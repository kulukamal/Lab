import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
a = 2
b = 2
c = 2

img1 = Image.open('pout.tif').convert('L')
arr1 = np.array(img1, dtype = np.uint8)

img2 = Image.open('tire.tif').convert('L')
arr2 = np.array(img2, dtype = np.uint8)

negImg1 = [255] - arr1
negImg2 = [255] - arr2

logImg1 = c * np.log2(arr1 + [1])
logImg2 = c * np.log2(arr2 + [1])

powImg1 = a * (arr1 ** [b])
powImg2 = a * (arr2 ** [b])

print(powImg1)

plt.subplot(241)
plt.imshow(arr1,cmap='gray')

plt.subplot(242)
plt.imshow(negImg1,cmap='gray')

plt.subplot(243)
plt.imshow(logImg1,cmap='gray')

plt.subplot(244)
plt.imshow(powImg1,cmap='gray')

plt.subplot(245)
plt.imshow(arr2,cmap='gray')

plt.subplot(246)
plt.imshow(negImg2,cmap='gray')

plt.subplot(247)
plt.imshow(logImg2,cmap='gray')

plt.subplot(248)
plt.imshow(powImg2,cmap='gray')


plt.show()