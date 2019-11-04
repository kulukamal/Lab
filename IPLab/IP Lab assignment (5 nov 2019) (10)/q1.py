import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as fft
from PIL import Image

def MSE(a,b):
    M,N = a.shape
    err = 0
    for i in range(M):
        for j in range(N):
            err += (a[i,j]-b[i,j])**2
    return err/(M*N)

def conv_row(input, filter):
    M,N = input.shape
    output = np.zeros((M,N), dtype= np.float)

    for i in range(M):
        for j in range(N):
            if j == N-1 :
                output[i,j] = input[i,j] * filter[0]
            else :
                output[i,j] = (input[i,j] * filter[0] + input[i,j+1] * filter[1]) / 2
    return output

def conv_col(input, filter):
    M,N = input.shape
    output = np.zeros((M,N), dtype= np.float)

    for i in range(M):
        for j in range(N):
            if i == M-1 :
                output[i,j] = input[i,j] * filter[0]
            else :
                output[i,j] = (input[i,j] * filter[0] + input[i+1,j] * filter[1]) / 2
    return output

def col_down(input):
    M,N = input.shape
    output = np.zeros((M,int(N/2)), dtype= np.float)

    for i in range(int(N/2)):
        output[:,i] = input[:,2*i]
    
    return output
def col_up(input):
    M,N = input.shape
    output = np.zeros((M,2*N), dtype= np.float)

    for i in range(2*N):
        output[:,i] = input[:,int(i/2)]
    
    return output
def row_down(input):
    M,N = input.shape
    output = np.zeros((int(M/2),N), dtype= np.float)

    for i in range(int(M/2)):
        output[i,:] = input[2*i,:]
    
    return output

def row_up(input):
    M,N = input.shape
    output = np.zeros((2*M,N), dtype= np.float)

    for i in range(2*M):
        output[i,:] = input[int(i/2),:]
    
    return output

img = Image.open('cameraman.tif').convert('L')
arr = np.array(img, dtype = np.float)
arr = arr / 255
M,N = arr.shape
transArr = np.zeros((M,N), dtype=np.float)
recArr = np.zeros((M,N), dtype=np.float)
lowPasssR = [0.7071068, 0.7071068]
highPassR = [0.7071068, -0.7071068]
lowPasssF = [0.7071068, 0.7071068]
highPassF = [-0.7071068, 0.7071068]

tmp1 = conv_row(arr, highPassF)
tmp2 = conv_row(arr, lowPasssF)

tmp1 = col_down(tmp1)
tmp2 = col_down(tmp2)

Wd = conv_col(tmp1,highPassF)
Wv = conv_col(tmp1,lowPasssF)
Wh = conv_col(tmp2,highPassF)
Wo = conv_col(tmp2,lowPasssF)

Wd = row_down(Wd)
Wv = row_down(Wv)
Wh = row_down(Wh)
Wo = row_down(Wo)
m = int(M/2)
n = int(N/2)
for i in range(m):
    for j in range(n):
        transArr[i,j] = Wd[i,j]
        transArr[i+m,j] = Wv[i,j]
        transArr[i,j+n] = Wh[i,j]
        transArr[i+m, j+n] = Wo[i,j]


plt.subplot(131)
plt.imshow(arr, cmap = 'gray')
plt.subplot(132)
plt.imshow(transArr, cmap = 'gray')

Wd = row_up(Wd)
Wh = row_up(Wh)
Wv = row_up(Wv)
Wo = row_up(Wo)

Wd = conv_col(Wd, highPassR)
Wh = conv_col(Wh, highPassR)
Wv = conv_col(Wv, lowPasssR)
Wo = conv_col(Wo, lowPasssR)

tmp1 = Wd + Wv
tmp2 = Wh + Wo

tmp1 = col_up(tmp1)
tmp2 = col_up(tmp2)

tmp1 = conv_row(tmp1, highPassR)
tmp2 = conv_row(tmp2, lowPasssR)

recArr = tmp1 + tmp2
print(MSE(arr,recArr))
plt.subplot(133)
plt.imshow(recArr, cmap='gray')
plt.show()

