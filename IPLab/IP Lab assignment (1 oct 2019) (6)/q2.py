import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
import math
import random
import skimage

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
wMax = 7
w = 3
arrMedian = np.zeros((r,c),dtype = np.uint8)
arrMedianStandad = np.zeros((r,c),dtype = np.uint8)
for i in range(r):
    for j in range(c):
        Median = []
        for k in range(-int(w/2),int(w/2)+1):
            for l in range(-int(w/2),int(w/2)+1):
                if (i+k >= 0 and i+k <r) and (j+l >=0 and j+l < c):
                    Median.append(arrNoise[i+k,j+l])
        Median.sort()
        arrMedianStandad[i,j] = Median[int(len(Median)/2)]

for i in range(r):
    for j in range(c):
        Median = []
        for k in range(-int(w/2),int(w/2)+1):
            for l in range(-int(w/2),int(w/2)+1):
                if (i+k >= 0 and i+k <r) and (j+l >=0 and j+l < c):
                    Median.append(arrNoise[i+k,j+l])
        Median.sort()
        median = int(Median[int(len(Median)/2)])
        Max = int(Median[len(Median)-1])
        Min = int(Median[0])
        b1 = median - Max
        b2 = median - Min

        if b1 < 0 and b2 > 0 :
            z1 = int(arrNoise[i,j] - Max)
            z2 = int(arrNoise[i,j] - Min)
            if z1 < 0 and z2 > 0:
                arrMedian[i,j] = arrNoise[i,j]
                w = 3
            else :
                arrMedian[i,j] = median
                w = 3
        else :
            w += 2
            if w <= wMax:
                j -= 1
            else:
                arrMedian[i,j] = arrNoise[i,j]
                w = 3 
plt.subplot(141)
plt.gca().set_title('Orginal Image')
plt.imshow(arr,cmap = 'gray')
plt.subplot(142)
plt.gca().set_title('With Noise')
plt.imshow(arrNoise,cmap = 'gray')
plt.subplot(143)
plt.gca().set_title('Median Filter, PSNR = '+ str(PSNR(arr,arrMedianStandad)))
plt.imshow(arrMedian,cmap = 'gray')
plt.subplot(144)
plt.gca().set_title('adaptive Median Filter, PSNR = '+ str(PSNR(arr,arrMedian)))
plt.imshow(arrMedian,cmap = 'gray')
plt.show()