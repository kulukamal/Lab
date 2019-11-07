import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import queue


Table = {'a':0.7,'b':0.1,'n':0.2}
sym = {'a':1, 'b':2, 'n':3}
revSym = {1:'a', 2:'b', 3:'n'}
seq = 'bana'
F = [0,0.7,0.8,1]
l = 0
u = 1
lnt = len(seq)
for s in seq:
    L = l + (u - l) * F[sym[s] - 1]
    U = l + (u - l) * F[sym[s]]
    l = L
    u = U
    print(l,u)
encodedMsg = (l+u) / 2
decodedMsg = ''
while lnt:
    for i in range(len(F)-1):
        if encodedMsg >= F[i] and encodedMsg < F[i+1]:
            decodedMsg += revSym[i+1]
            encodedMsg = (encodedMsg - F[i]) / (F[i+1] - F[i])
            break
    lnt -= 1
print(decodedMsg)


