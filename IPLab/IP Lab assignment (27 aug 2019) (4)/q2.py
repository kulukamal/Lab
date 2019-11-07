import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

r = int(input('row = '))
c = int(input('col = '))

arr = np.zeros((r ,c ), dtype = np.float)

for i in range(r):
    for j in range(c):
        arr[i,j] = float(input())
print(arr)
print('-conv----------')
R = int(input('row = '))
C = int(input('col = '))

tmp = np.zeros((R, C), dtype = np.float)
conv = np.zeros((R, C), dtype = np.float)

for i in range(R):
    for j in range(C):
        tmp[i,j] = float(input())

for i in range(R):
    for j in range(C):
        conv[i,j] = tmp[R-1-i,C-1-j]

print(tmp)

proArr = np.zeros((r+2,c+2), dtype = np.float)
finalArr = np.zeros((r,c), dtype = np.float)
proArr[int(R/2) : int(R/2) + r , int(C/2) : int(C/2) + c] = arr
print('-------------')
# print(proArr)
for i in range(r):
    for j in range(c):
        s = 0
        for k in range(R):
            for l in range(C):
                s += proArr[i+k,j+l] * conv[k,l]
        finalArr[i,j] = s
print(finalArr)

outMat = np.zeros((r+R-1,c+C-1), dtype = np.float)
multi = np.zeros(((r+R-1)*(c+C-1), r*c), dtype = np.float)
flat = np.zeros((r*c), dtype = np.float)
padZero = np.zeros((r+R-1,c+C-1), dtype = np.float)
flatPadZero = np.zeros(((r+R-1)*(c+C-1)), dtype = np.float)
for i in range(R):
    for j in range(C):
        padZero[i,j] = tmp[i,j]
print(padZero)

for i in range(r+R-1):
    for j in range(c+C-1):
        flatPadZero[i*(c+C-1) + j] = padZero[i,j]

for i in range(r):
    for j in range(c):
        flat[i*c+j] = arr[i,j]
print(flatPadZero)
print(flat)
for i in range(r*c):
    for j in range(i+ int(i/c),(r+R-1)*(c+C-1)):
        multi[j,i] = flatPadZero[j-i - int(i/c)]
print(multi)
ans = np.dot(multi,flat)
final = ans.reshape((r+R-1,c+C-1))
print(final)
print(np.convolve(arr,tmp))