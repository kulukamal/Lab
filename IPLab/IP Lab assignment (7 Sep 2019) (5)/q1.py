import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ar = np.zeros((8,8), dtype = np.float)
ai = np.zeros((8,8), dtype = np.float)
M,N = ar.shape
basisR = np.zeros((M*M,N*N), dtype = np.float)
basisI = np.zeros((M*M,N*N), dtype = np.float)

for i in range(M):
    for j in range(N):
        ar[i,j] = np.cos((-2 * np.pi * i * j)/M)
        ai[i,j] = np.sin((-2 * np.pi * i * j)/M)

for u in range(M):
    for v in range(N):
        for i in range(M):
            for j in range(N):
                basisR[u*M+i,v*N+j] = ar[i,u] * ar[j,v] - ai[i,u] * ai[j,v]
                basisI[u*M+i,v*N+j] = ar[i,u] * ai[j,v] + ai[i,u] * ar[j,v]
Real = np.asarray(basisR * 255,dtype=np.uint8)
Img =  np.asarray(basisI * 255,dtype=np.uint8)
print(Img[0:8,0:8])
plt.subplot(1,2,1)
plt.imshow(Real, cmap = 'gray')
plt.subplot(122)
plt.imshow(Img,cmap = 'gray')
plt.show()
