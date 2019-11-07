import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
import math

img = Image.open('test.png').convert('L')
imgArr = np.asarray(img,dtype=np.uint8)
imgOut = np.zeros(imgArr.shape,dtype=np.uint8)
vis = np.zeros(imgArr.shape, dtype = np.uint8)
label = np.zeros(imgArr.shape, dtype = np.uint8)
maxLabel = 1
max
equi = []
r,c  = imgArr.shape
label2 = np.zeros((r*c),dtype = np.int32)
maxLabel2 = 1
for i in range(r):
    for j in range(c):
        if imgArr[i,j] == 255:
            if i == 0 and j == 0 :
                label[i,j] = maxLabel
                maxLabel += 1
            elif i == 0 :
                if label[i,j-1] != 0:
                    label[i,j] = label[i,j-1]
                else:
                    label[i,j] = maxLabel
                    maxLabel += 1
            elif j == 0 :
                if label[i-1,j] != 0:
                    label[i,j] = label[i-1,j]
                else:
                    label[i,j] = maxLabel
                    maxLabel += 1
            else :
                if label[i,j-1] == 0 and label[i-1,j] == 0:
                    label[i,j] = maxLabel
                    maxLabel += 1
                elif label[i,j-1] != 0  and label[i-1,j] != 0:
                    label[i,j] = np.minimum(label[i,j-1],label[i-1,j])
                    if label[i,j-1] != label[i-1,j]:
                        if label2[label[i,j-1]] == 0 and label2[label[i-1,j]] != 0 :
                            label2[label[i,j-1]] = label2[label[i-1,j]]
                        elif label2[label[i,j-1]] != 0 and label2[label[i-1,j]] == 0 :
                            label2[label[i-1,j]] = label2[label[i,j-1]]
                        else:
                            label2[label[i-1,j]] = label2[label[i,j-1]] = maxLabel2
                            maxLabel2 += 1

                else:
                    label[i,j] = np.maximum(label[i,j-1],label[i-1,j])
print(label2)
print(maxLabel2)    
plt.subplot(211)
plt.imshow(img, cmap = 'gray')
plt.subplot(212)
plt.imshow(imgOut, cmap = 'gray')
plt.show()
