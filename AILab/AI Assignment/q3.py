import numpy as np
import numpy.linalg as la
from matplotlib import pyplot as plt
from PIL import Image
N = 425 * 425
arr = np.zeros((N,25), dtype= np.float)
X = np.zeros((N,25), dtype= np.float)
for i in range(1,26):
    img = Image.open('Eigenfaces/Train/'+ str(i) +'.jpg').convert('L')
    tmp = np.asarray(img, dtype=np.uint8)
    k = 0
    for l in range(425):
        for m in range(425):
            arr[k,i-1] = tmp[l,m]
            k += 1
mu = np.zeros((N,), dtype= np.float)
for i in range(N):
    mu[i] = np.mean(arr[i,:])

for i in range(N):
    for j in range(25):
        X[i,j] = arr[i,j] - mu[i]

C = np.cov(np.dot(X.T,X))
w,v = la.eig(C)

shi = v[:,0:20]
phi = np.dot(shi.T,X.T)

omega = np.dot(phi,X)

tst = Image.open('Eigenfaces\Test\S074_005_00222617.jpg').convert('L')
test = np.asarray(tst, dtype= np.float)
test = test.reshape((N,))
test = test - mu

t = np.dot(phi,test)

res1 = -1
res2 = -1
for i in range(25):
    tmp = np.sum(np.dot((omega[:,i].T-t), (omega[:,i].T-t).T))
    if tmp < res2 or res2 < 0:
        res1 = i+1
        res2 = tmp

out = Image.open('Eigenfaces/Train/' + str(res1) + '.jpg').convert('L')

plt.subplot(121)
plt.imshow(tst, cmap='gray')
plt.subplot(122)
plt.imshow(out, cmap= 'gray')
plt.show()