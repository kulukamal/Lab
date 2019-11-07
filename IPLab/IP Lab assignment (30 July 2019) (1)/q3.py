from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure()
def z_function(x, y):
    return 255*(math.cos(2*math.pi*(x/50 + y/25)))

arr = np.zeros((512,512),dtype=np.uint8)

for x in range(0,512):
    for y in range(0,512):
        arr[x,y] = z_function(x, y)

plt.imshow(arr, cmap='gray')
plt.show()
