import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('fractal.png').convert('L')
arr = np.array(img, dtype = np.uint8)
r,c = arr.shape
bitPlanes = np.ndarray((8,r,c), dtype = np.uint8)

for i in range(r):
    for j in range(c):
        binStr = np.binary_repr(arr[i,j],width=8)
        for k in range(8):
            bitPlanes[k,i,j] = int(binStr[k])


for i in range(8):
    plt.figure('bit plane-' + str(7-i))
    plt.imshow(bitPlanes[i],cmap='gray')

plt.show()
