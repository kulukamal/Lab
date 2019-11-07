import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as fft
from PIL import Image

img = Image.open('cameraman.tif').convert('L')
arr = np.array(img, dtype = np.float)
M,N = arr.shape


DCT = np.zeros((N,N),dtype = np.complex_)
for i in range(N):
        for j in range(N):
            if i==0 :
                DCT[i,j] = np.sqrt(np.float(1/M))*np.cos((np.pi * (2*j + 1) * i) / (2*M))
            else:
                DCT[i,j] = np.sqrt(np.float(2/M))*np.cos((np.pi * (2*j + 1) * i) / (2*M))


fImg = np.dot(np.dot(DCT,arr),np.transpose(DCT))
for i in range(128,200):
    for j in range(128,200):
        fImg[i,j] = 0
rImg1 = np.dot(np.dot(np.transpose(DCT),fImg),DCT).real
for i in range(64,200):
    for j in range(64,200):
        fImg[i,j] = 0
rImg2 = np.dot(np.dot(np.transpose(DCT),fImg),DCT).real
for i in range(32,200):
    for j in range(32,200):
        fImg[i,j] = 0
rImg3 = np.dot(np.dot(np.transpose(DCT),fImg),DCT).real
plt.subplot(221)
plt.imshow(img, cmap = 'gray')
plt.subplot(222)
plt.imshow(rImg1, cmap = 'gray')
plt.subplot(223)
plt.imshow(rImg2, cmap = 'gray')
plt.subplot(224)
plt.imshow(rImg3, cmap = 'gray')
plt.show()