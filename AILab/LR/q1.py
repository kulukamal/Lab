import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from numpy import linalg as LA
import os


x = np.array([50,53,54,55,56,59,62,65,67,71,72,74,75,76,79,80,82,85,87,90,93,94,95,97,100])
y = np.array([122,118,128,121,125,136,144,142,149,161,167,168,162,171,175,182,180,183,188,200,194,206,207,210,219])

N = x.shape[0]
M = y.shape[0]
print(N,M)

X = 0
Y = 0
XY = 0
X2 = 0
Y2 = 0

for i in range(N):
    X += x[i]
    Y += y[i]
    XY += x[i]*y[i]
    X2 += (x[i]*x[i])
    Y2 += (y[i]*y[i])


w1 = float(Y*X2-X*XY) / (N*X2-X**2)
w2 = float(X*Y-N*XY)/(X**2-N*X2)

X_ = [i for i in range(45,105)]
Y_ = [w1+w2*x for x in X_]

plt.scatter(x,y)
plt.plot(X_,Y_)
plt.show()

