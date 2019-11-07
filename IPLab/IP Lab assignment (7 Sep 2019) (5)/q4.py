import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as fft
from PIL import Image

img = Image.open('cameraman.tif').convert('L')
arr = np.array(img, dtype = np.float)
M,N = arr.shape


DFT = np.zeros((N,N),dtype = np.complex_)
for i in range(N):
        for j in range(N):
                DFT[i,j] = (np.exp(-(2j*np.pi)/N)**(i*j))/np.sqrt(N)
DFTC = np.conj(DFT)

fImg = np.dot(np.dot(DFT,arr),np.transpose(DFT))
spectrum = fImg.real - np.min(fImg.real)
spectrum = (spectrum*255) / np.max(spectrum)
print(spectrum)
rImg = np.dot(np.dot(np.transpose(DFTC),fImg),DFTC).real
plt.subplot(131)
plt.imshow(img, cmap = 'gray')
plt.subplot(132)
plt.imshow(spectrum, cmap = 'gray')
plt.subplot(133)
plt.imshow(rImg, cmap = 'gray')
plt.show()