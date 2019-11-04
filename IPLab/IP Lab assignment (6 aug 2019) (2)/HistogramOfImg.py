import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('grain.png').convert('L')
arr = np.array(img, dtype = np.uint8)
hist = np.zeros((256), dtype = np.int32)
r,c = arr.shape
for i in range(r):
    for j in range(c):
        hist[arr[i,j]] += 1

plt.figure('barChart')
plt.bar(range(256), hist)
plt.show()