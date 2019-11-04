import matplotlib
import matplotlib.pyplot as plt
import numpy as np

height = width = 256


img = np.zeros((256,256), np.uint8)
d = int(input("enter value : "))
img[30:226,30:226] = 255
img[30+d:226-d,30+d:226-d] = 0
plt.imshow(img, cmap = 'gray', vmin=0, vmax=255)