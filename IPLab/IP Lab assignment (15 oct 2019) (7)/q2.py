import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as fft
from PIL import Image

img = Image.open('cameraman.tif').convert('L')
arr = np.array(img, dtype = np.float)
M,N = arr.shape
H = np.zeros((N,N), dtype = np.complex_)
H1 = np.zeros((N,N), dtype = np.complex_)
k = 0.0001
DFT = np.zeros((N,N),dtype = np.complex_)
for i in range(N):
        for j in range(N):
                DFT[i,j] = (np.exp(-(2j*np.pi)/N)**(i*j))/np.sqrt(N)
                H[i,j] = np.exp(-k*np.float_power((i*i+j*j),(5/6)))
                fact = np.pi*(0.001*(i+1)+0.1*(j+1))
                H1[i,j] = (np.sin(fact)*np.exp(-1j*fact))/(fact)
DFTC = np.conj(DFT)
# fact = np.pi*(0.001*i+0.1*j)
# H[i,j] = (np.sin(fact)*np.exp(-1j*fact))/(fact)
fImg = np.dot(np.dot(DFT,arr),np.transpose(DFT))
b1Img = fImg * H
b2Img = fImg * H1
n1 = np.random.normal(0,1,(N,N))
noise = np.clip(n1,0,255)
r1Img = np.dot(np.dot(np.transpose(DFTC),b1Img),DFTC) + noise
r2Img = np.dot(np.dot(np.transpose(DFTC),b2Img),DFTC) + noise
f1Img = np.dot(np.dot(DFT,r1Img),np.transpose(DFT))
f2Img = np.dot(np.dot(DFT,r2Img),np.transpose(DFT))
W = np.zeros((N,N), dtype=np.complex_)
W1= np.zeros((N,N), dtype=np.complex_)
k = 0.0005
k1 = 0.001
for i in range(N):
    for j in range(N):
        W[i,j] = np.conj(H[i,j])/(np.conj(H[i,j])*H[i,j] + k)
        # W[i,j] = 1/H[i,j] 
        W1[i,j] = np.conj(H1[i,j])/(np.conj(H1[i,j])*H1[i,j] + k1)
        # W1[i,j] = 1/H1[i,j] 
fb1Img = f1Img * W
fb2Img = f2Img * W1
fr1Img = np.dot(np.dot(np.transpose(DFTC),fb1Img),DFTC).real
fr2Img = np.dot(np.dot(np.transpose(DFTC),fb2Img),DFTC).real
plt.subplot(231)
plt.imshow(arr, cmap = 'gray')
plt.subplot(232)
plt.imshow(r1Img.real, cmap = 'gray')
plt.subplot(233)
plt.imshow(r2Img.real, cmap = 'gray')
plt.subplot(235)
plt.imshow(fr1Img, cmap = 'gray')
plt.subplot(236)
plt.imshow(fr2Img, cmap = 'gray')
plt.show()