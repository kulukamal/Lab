import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('cameraman.tif')
arr = np.array(img)
k = int(input("(+|-)x : "))
r,c = arr.shape
imarr = np.zeros((r*k, c*k), dtype=np.uint8)
imarr2 = np.zeros((int(r/k), int(c/k)), dtype=np.uint8)
for i in range(0,r*k):
    for j in range(0,c*k):
        imarr[i,j] = arr[int(i/k),int(j/k)]

for i in range(0,r):
    for j in range(0,c):
        if i % k == 0 and j % k == 0:
            imarr2[int(i/k),int(j/k)] = arr[i,j]
finalImgZoomIn = Image.fromarray(imarr)
finalImgZoomIn.save('finalImgZoomIn.tif')
finalImgOut = Image.fromarray(imarr)
finalImgOut.save('finalImgOut.tif')
plt.figure("0")
plt.imshow(arr, cmap='gray')
plt.figure("1")
plt.imshow(imarr, cmap='gray')
plt.figure("2")
plt.imshow(imarr2, cmap='gray')
plt.show()
