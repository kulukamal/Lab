import numpy as np
import numpy.linalg as la
from matplotlib import pyplot as plt
from PIL import Image

img1 = Image.open('1.gif').convert('L')
img2 = Image.open('2.gif').convert('L')
img3 = Image.open('3.gif').convert('L')
img4 = Image.open('4.gif').convert('L')

arr1 = np.asarray(img1, dtype=np.uint8)
arr2 = np.asarray(img2, dtype=np.uint8)
arr3 = np.asarray(img3, dtype=np.uint8)
arr4 = np.asarray(img4, dtype=np.uint8)

M,N = arr1.shape

X = np.zeros((M*N,4), dtype= np.float)
XNorm = np.zeros((M*N,4), dtype= np.float)
k = 0
for i in range(M):
    for j in range(N):
        X[k,0] = arr1[i,j]
        X[k,1] = arr2[i,j]
        X[k,2] = arr3[i,j]
        X[k,3] = arr4[i,j]
        k += 1
Xmean = np.zeros((4) , dtype= np.float)
Xmean[0] = np.mean(X[:,0])
Xmean[1] = np.mean(X[:,1])
Xmean[2] = np.mean(X[:,2])
Xmean[3] = np.mean(X[:,3])

for i in range(M*N):
    XNorm[i,0] = X[i,0] - Xmean[0] 
    XNorm[i,1] = X[i,1] - Xmean[1] 
    XNorm[i,2] = X[i,2] - Xmean[2] 
    XNorm[i,3] = X[i,3] - Xmean[3] 

C = np.dot(XNorm.T,XNorm)
print(C)
w, v = la.eig(C)
print(w)
print(v)

PC1 = np.zeros((M,N), dtype=np.float)
PC2 = np.zeros((M,N), dtype=np.float)
PC3 = np.zeros((M,N), dtype=np.float)
PC4 = np.zeros((M,N), dtype=np.float)

Y = np.dot(XNorm, v)

for i in range(M):
    for j in range(N):
        PC1[i,j] = Y[i * N + j, 0]
        PC2[i,j] = Y[i * N + j, 1]
        PC3[i,j] = Y[i * N + j, 2]
        PC4[i,j] = Y[i * N + j, 3]
plt.subplot(221)
plt.imshow(PC1, cmap='gray')
plt.subplot(222)
plt.imshow(PC2, cmap='gray')
plt.subplot(223)
plt.imshow(PC3, cmap='gray')
plt.subplot(224)
plt.imshow(PC4, cmap='gray')
plt.show()