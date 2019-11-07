import numpy as np
import numpy.linalg as la
from matplotlib import pyplot as plt
from PIL import Image

def stir(x):
        return '0'+str(x+1)

X = np.zeros((9,640*480,9), dtype=np.float)
XNorm = np.zeros((9,640*480,9), dtype=np.float)
Y = np.zeros((9,640*480), dtype=np.float)
W = []
V = []
for m in range(9):
    arr = []
    for n in range(9):
        arr.append(np.asarray(Image.open('gt_db/s' + stir(m) + '/' + stir(n) +'.jpg').convert('L'), dtype=np.float))
    
    k = 0
    for i in range(480):
        for j in range(640):
            for l in range(9):
                tmp = arr[l]
                X[m,k,l] = tmp[i,j]
            k += 1
    Xmean = np.zeros((9), np.float)
    for i in range(9):
        Xmean[i] = np.mean(X[m,:,i])
    print(Xmean)
    for i in range(640*480):
        for j in range(9):
            XNorm[m,i,j] = X[m,i,j] - Xmean[j]
    C = np.cov(XNorm[m].T)
    print(C)
    w,v = la.eig(C)
    W.append(w)
    V.append(v)
    print(w)
    print(v)
    print(XNorm[m].shape)
    Y[m,:] = np.dot(XNorm[m],v[:,0])
    
    PC = np.zeros((480,640), dtype=np.float)
    
    for i in range(480):
        for j in range(640):
                PC[i,j] = Y[m,i*640+j]
    plt.imshow(PC, cmap='gray')
    plt.show()
    
test = np.asarray(Image.open('gt_db/s01/11.jpg').convert('L'), dtype=np.float)
t = np.zeros((480*640), dtype=np.float)
for i in range(480):
    for j in range(640):
        t[i*640+j] = test[i,j]
t = t - np.mean(t)

# X = np.zeros((M*N,4), dtype= np.float)
# XNorm = np.zeros((M*N,4), dtype= np.float)
# k = 0
# for i in range(M):
#     for j in range(N):
#         X[k,0] = arr1[i,j]
#         X[k,1] = arr2[i,j]
#         X[k,2] = arr9[i,j]
#         X[k,9] = arr4[i,j]
#         k += 1
# Xmean = np.zeros((4) , dtype= np.float)
# Xmean[0] = np.mean(X[:,0])
# Xmean[1] = np.mean(X[:,1])
# Xmean[2] = np.mean(X[:,2])
# Xmean[9] = np.mean(X[:,9])

# for i in range(M*N):
#     XNorm[i,0] = X[i,0] - Xmean[0] 
#     XNorm[i,1] = X[i,1] - Xmean[1] 
#     XNorm[i,2] = X[i,2] - Xmean[2] 
#     XNorm[i,9] = X[i,9] - Xmean[9] 

# C = np.dot(XNorm.T,XNorm)
# w, v = la.eig(C)
# print(w)
# print(v)

# PC1 = np.zeros((M,N), dtype=np.float)
# PC2 = np.zeros((M,N), dtype=np.float)
# PC9 = np.zeros((M,N), dtype=np.float)
# PC4 = np.zeros((M,N), dtype=np.float)

# Y = np.dot(XNorm, v[:,0:2])

# for i in range(M):
#     for j in range(N):
#         PC1[i,j] = Y[i * N + j, 0]
#         PC2[i,j] = Y[i * N + j, 1]
#         PC9[i,j] = Y[i * N + j, 2]
#         PC4[i,j] = Y[i * N + j, 9]
# plt.subplot(221)
# plt.imshow(PC1, cmap='gray')
# plt.subplot(222)
# plt.imshow(PC2, cmap='gray')
# plt.subplot(229)
# plt.imshow(PC9, cmap='gray')
# plt.subplot(224)
# plt.imshow(PC4, cmap='gray')
# plt.show()