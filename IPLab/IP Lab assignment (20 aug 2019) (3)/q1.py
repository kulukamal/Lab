import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2

img = Image.open('tire.tif').convert('L')

imgArr = np.array(img, dtype = np.uint8)
newImgArr = np.array(img, dtype = np.uint8)
sysImgArr = np.array(img, dtype = np.uint8)

hist = np.zeros((256), dtype = np.int32)
newHist = np.zeros((256), dtype = np.int32)
sysHist = np.zeros((256), dtype = np.int32)
r,c = imgArr.shape
sysImgArr = cv2.equalizeHist(imgArr)
for i in range(r):
    for j in range(c):
        hist[imgArr[i,j]] += 1
        sysHist[sysImgArr[i,j]] += 1

pdf = np.zeros((256), dtype = np.float)
cdf = np.zeros((256), dtype = np.float)
newMap = np.zeros((256), dtype = np.uint8)
for i in range(256):
    pdf[i] = hist[i] / (r*c)
    if i != 0 :
        cdf[i] = pdf[i] + cdf[i-1]
    else:
        cdf[i] = pdf[i]
    newMap[i] = round(cdf[i] * 255)
for i in range(r):
    for j in range(c):
        newImgArr[i,j] = newMap[imgArr[i,j]]

for i in range(r):
    for j in range(c):
        newHist[newImgArr[i,j]] += 1



plt.subplot(3,2,1)
plt.imshow(imgArr,cmap='gray')
plt.subplot(3,2,2)
plt.bar(range(256), hist)
plt.subplot(3,2,3)
plt.imshow(sysImgArr,cmap='gray')
plt.subplot(3,2,4)
plt.bar(range(256), sysHist)
plt.subplot(3,2,5)
plt.imshow(newImgArr,cmap='gray')
plt.subplot(3,2,6)
plt.bar(range(256), newHist)



plt.show()