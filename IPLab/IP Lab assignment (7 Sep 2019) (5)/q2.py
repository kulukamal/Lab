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
        if j == 0 :
            ar[i,j] = np.sqrt(np.float(1/M))*np.cos((np.pi * (2*i + 1) * j) / (2*M))
        else:
            ar[i,j] = np.sqrt(np.float(2/M))*np.cos((np.pi * (2*i + 1) * j) / (2*M))

for u in range(M):
    for v in range(N):
        for i in range(M):
            for j in range(N):
                basisR[u*M+i,v*N+j] = ar[i,u] * ar[j,v]
Real = np.asarray(basisR * 255,dtype=np.uint8)
plt.subplot(111)
plt.imshow(Real, cmap = 'gray')
plt.show()
