import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

global coordsX, coordsY
coordsX = []
coordsY = []

sampleSize = 50
sampleName = "River"

def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata

    # print 'x = %d, y = %d'%(
    #     ix, iy)

    # assign global variable to access outside of function
    coordsX.append(int(ix))
    coordsY.append(int(iy))
    print(len(coordsX))
    # Disconnect after 2 clicks
    if len(coordsX) == sampleSize:
        sampleX = np.asarray(coordsX,dtype=np.int16)
        sampleY = np.asarray(coordsY,dtype=np.int16)
        np.save(sampleName+"X",sampleX)
        np.save(sampleName+"Y",sampleY)
        fig.canvas.mpl_disconnect(cid)
        plt.close(1)
    return


img = Image.open("band4.gif")
arr = np.asarray(img)

print(arr)

fig = plt.figure("1")
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.imshow(arr)
plt.show()