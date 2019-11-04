import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as fft
from PIL import Image
import numpy.linalg as li

def MSE(a,b):
    m,n = a.shape
    err = 0
    for i in range(m):
        for j in range(n):
            err += (a[i,j]-b[i,j])**2
    err /= (m*n)
    return err

img = Image.open('cameraman.tif').convert('L')
arr = np.array(img, dtype = np.float)

M,N = arr.shape
X = np.zeros((M,N), dtype = np.float)

mu = np.zeros((N,), dtype= np.float)

for i in range(N):
    mu[i] = np.mean(arr[:,i])

for i in range(M):
    for j in range(N):
        X[i,j] = arr[i,j] - mu[j]

Cov = np.cov(np.dot(X.T, X))
w,v = li.eig(Cov)

mse = []
x = []
k = 1
while k < N :
    T = v.T[0:k+1,:]     
    Y = np.dot(T,X)
    X_restore = np.dot(T.T,Y)
    for i in range(M):
        for j in range(N):
            X_restore[i,j] = X_restore[i,j] + mu[j]
    mse.append(MSE(arr,X_restore))
    x.append(k)
    k = k + 10
    plt.subplot(131)
    plt.imshow(arr, cmap= 'gray')
    plt.subplot(132)
    plt.imshow(X_restore.real, cmap= 'gray')
    plt.subplot(133)
    plt.plot(x,mse)
    plt.xlabel('no of eigen vectors')
    plt.ylabel('mse')
    plt.show()
T = v.T[0:N,:]     
Y = np.dot(T,X)
X_restore = np.dot(T.T,Y)
for i in range(M):
    for j in range(N):
        X_restore[i,j] = X_restore[i,j] + mu[j]
mse.append(MSE(arr,X_restore))
x.append(N-1)
plt.subplot(131)
plt.imshow(arr, cmap= 'gray')
plt.subplot(132)
plt.imshow(X_restore.real, cmap= 'gray')
plt.subplot(133)
plt.plot(x,mse)
plt.xlabel('no of eigen vectors')
plt.ylabel('mse')
plt.show()