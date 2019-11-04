import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


img = Image.open('eight.tif').convert('L')
arr = np.array(img, dtype = np.uint8)
finalArr1 = np.array(img, dtype = np.uint8)
finalArr2 = np.array(img, dtype = np.uint8)
r,c = arr.shape
mask1 = np.asarray([[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]) / [9]
mask2 = np.asarray([[1, 2, 1],
         [2, 4, 2],
         [1, 2, 1]]) / [16]
R,C = mask1.shape
proArr =  np.zeros((r+2,c+2), dtype = np.float)
proArr[int(R/2) : int(R/2) + r , int(C/2) : int(C/2) + c] = arr
for i in range(r):
    for j in range(c):
        s = 0
        for k in range(R):
            for l in range(C):
                s += proArr[i+k,j+l] * mask1[k,l]
        finalArr1[i,j] = int(s)
# print(finalArr1)

for i in range(r):
    for j in range(c):
        s = 0
        for k in range(R):
            for l in range(C):
                s += proArr[i+k,j+l] * mask2[k,l]
        finalArr2[i,j] = int(s)
# print(finalArr2)

plt.subplot(131)
plt.imshow(arr, cmap='gray')
plt.subplot(132)
plt.imshow(finalArr1, cmap='gray')
plt.subplot(133)
plt.imshow(finalArr2,cmap='gray')
plt.show()