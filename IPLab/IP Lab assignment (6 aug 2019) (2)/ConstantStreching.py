import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def strechFunc(x):
    if x >=0 and x<= 80:
        return int(x/2)
    if x > 80 and x <= 160:
        return int((5 * (x - 80)) / 2) + 40
    if x > 160 and x <= 255:
        return int((55*(x - 160))/95) + 200

img = Image.open('grain.png').convert('L')
arr = np.array(img, dtype = np.uint8)

r,c = arr.shape
for i in range(r):
    for j in range(c):
        arr[i,j] = strechFunc(arr[i,j])

hist = np.zeros((256), dtype = np.int32)
for i in range(r):
    for j in range(c):
        hist[arr[i,j]] += 1

ConstantStreching = Image.fromarray(arr)
ConstantStreching.save('EnhancedGrain.png')

plt.figure('barChart')
plt.bar(range(256), hist)
plt.figure('Constant streching')
plt.imshow(arr, cmap= 'gray')
plt.show()