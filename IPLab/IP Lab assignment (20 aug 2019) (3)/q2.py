import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2

def revMap(value, mapIn, mapOut):
    s = mapIn[value]
    z = -1
    diff = 100000000
    for i in range(256):
        if diff > abs(s - mapOut[i]):
            z = i
            diff = abs(s-mapOut[i])
    return z

imgIn = Image.open('tire.tif').convert('L')
imgOut = Image.open('cameraman.tif').convert('L')

ImgArrIn = np.array(imgIn, dtype = np.uint8)
ImgArrOut = np.array(imgOut, dtype = np.uint8)
equalizedArr = np.array(imgIn, dtype = np.uint8)
finalImgArr = np.array(imgIn, dtype = np.uint8)

histIn = np.zeros((256), dtype = np.int32)
histOut = np.zeros((256), dtype = np.int32)

newMapIn = np.zeros((256), dtype = np.int32)
newMapOut = np.zeros((256), dtype = np.int32)

newHistIn = np.zeros((256), dtype = np.int32)
newHistOut = np.zeros((256), dtype = np.int32)
equalizedHist = np.zeros((256), dtype = np.int32)
finalHist = np.zeros((256), dtype = np.int32)

rIn,cIn = ImgArrIn.shape
rOut,cOut = ImgArrOut.shape

pdfIn = np.zeros((256), dtype=np.float)
pdfOut = np.zeros((256), dtype=np.float)

cdfIn = np.zeros((256), dtype=np.float)
cdfOut = np.zeros((256), dtype=np.float)

for i in range(rIn):
    for j in range(cIn):
        histIn[ImgArrIn[i,j]] += 1

for i in range(rOut):
    for j in range(cOut):
        histOut[ImgArrOut[i,j]] += 1

for i in range(256):
    pdfIn[i] = histIn[i] / (rIn * cIn)
    pdfOut[i] = histOut[i] / (rOut * cOut)
    if i != 0 :
        cdfIn[i] = pdfIn[i] + cdfIn[i-1]
        cdfOut[i] = pdfOut[i] + cdfOut[i-1]
    else:
        cdfIn[i] = pdfIn[i]
        cdfOut[i] = pdfOut[i]
    newMapIn[i] = round(cdfIn[i]*255)
    newMapOut[i] = round(cdfOut[i]*255)

for i in range(rIn):
    for j in range(cIn):
        finalImgArr[i,j] = revMap(ImgArrIn[i,j],newMapIn,newMapOut)
        equalizedArr[i,j] = newMapIn[ImgArrIn[i,j]]

for i in range(rIn):
    for j in range(cIn):
        finalHist[finalImgArr[i,j]] += 1
        equalizedHist[equalizedArr[i,j]] += 1


plt.subplot(4,2,1)
plt.imshow(ImgArrIn,cmap='gray')
plt.subplot(4,2,2)
plt.bar(range(256), histIn)
plt.subplot(4,2,3)
plt.imshow(ImgArrOut,cmap='gray')
plt.subplot(4,2,4)
plt.bar(range(256), histOut)
plt.subplot(4,2,5)
plt.imshow(equalizedArr,cmap='gray')
plt.subplot(4,2,6)
plt.bar(range(256), equalizedHist)
plt.subplot(4,2,7)
plt.imshow(finalImgArr,cmap='gray')
plt.subplot(4,2,8)
plt.bar(range(256), finalHist)
plt.show()