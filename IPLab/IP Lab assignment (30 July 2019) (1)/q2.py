import matplotlib.pyplot as plt
import numpy as np
from skimage import draw

arr = np.zeros((512, 512))
d = int(input('enter d :'))
# Create an outer and inner circle. Then subtract the inner from the outer.
radius = 100
ir= radius 
ora = radius + d

for i in range(0,512):
    for j in range(0,512):
        if (i-256)*(i-256) + (j-256)*(j-256) - ora*ora <= 0 and (i-256)*(i-256) + (j-256)*(j-256) - ir*ir > 0:
            arr[i,j]=255

plt.imshow(arr, cmap='gray')
plt.show()
