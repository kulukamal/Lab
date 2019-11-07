import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
import math
import random
def PSNR(imgA,imgB):
    mse = np.mean((imgA - imgB) ** 2)
    if mse == 0:
        return 100
    else:
        return 20 * math.log10(255 / math.sqrt(mse))


img = Image.open('cameraman.tif').convert('L')
arr = np.asarray(img,dtype=np.uint8)
p = 0.1
r,c = arr.shape

arrNoise = np.zeros((r,c),dtype = np.uint8)
for i in range(r):
    for j in range(c):
        if random.random() <= p :
            arrNoise[i,j] = random.randint(0,1) * 255
        else:
            arrNoise[i,j] = arr[i,j]
w = 3
arrMean = np.zeros((r,c),dtype = np.uint8)
arrMedian = np.zeros((r,c),dtype = np.uint8)
arrMin = np.zeros((r,c),dtype = np.uint8)
arrMax = np.zeros((r,c),dtype = np.uint8)

for i in range(r):
    for j in range(c):
        mean = 0
        Max = 0
        Min = 256
        Median = []
        for k in range(-int(w/2),int(w/2)+1):
            for l in range(-int(w/2),int(w/2)+1):
                if (i+k >= 0 and i+k <r) and (j+l >=0 and j+l < c):
                    mean+= arrNoise[i+k,j+l]
                    Max = np.maximum(Max,arrNoise[i+k,j+l])
                    Min = np.minimum(Min,arrNoise[i+k,j+l])
                    Median.append(arrNoise[i+k,j+l])
        arrMean[i,j] = int(mean/(w*w))
        arrMax[i,j] = Max
        arrMin[i,j] = Min
        Median.sort()
        arrMedian[i,j] = Median[int(len(Median)/2)]

plt.subplot(231)
plt.gca().set_title('Orginal Image')
plt.imshow(arr, cmap = 'gray')
plt.subplot(232)
plt.gca().set_title('With Noise')
plt.imshow(arrNoise, cmap = 'gray')
plt.subplot(233)
plt.gca().set_title('Mean Filter, PSNR = '+ str(PSNR(arr,arrMean)))
plt.imshow(arrMean, cmap = 'gray')
plt.subplot(234)
plt.gca().set_title('Median Filter, PSNR = '+ str(PSNR(arr,arrMedian)))
plt.imshow(arrMedian, cmap = 'gray')
plt.subplot(235)
plt.gca().set_title('Max Filter, PSNR = '+ str(PSNR(arr,arrMax)))
plt.imshow(arrMax, cmap = 'gray')
plt.subplot(236)
plt.gca().set_title('Min Filter, PSNR = '+str(PSNR(arr,arrMin)))
plt.imshow(arrMin, cmap = 'gray')
plt.show()
