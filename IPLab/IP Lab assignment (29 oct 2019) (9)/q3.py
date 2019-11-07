import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import queue

val = 256
decVal = 256
seq = 'KAMAL'
encodedMsg = ''
decodedMsg = ''
Table = {}
for i in range(0,256):
    Table[chr(i)] = i
print(seq)
P = seq[0]
C = 0
for i in range(1,len(seq)):
    C = seq[i]

    if Table.get(P+C) != None:
        P = P + C
    else:
        encodedMsg +=  str(Table[P]) + ' '
        Table[P+C] = val
        val += 1
        P = C
encodedMsg +=  str(Table[P])
print(encodedMsg)

listMsg = encodedMsg.split(' ')

decodeTable = {}
for i in range(0,256):
    decodeTable[str(i)] = chr(i)

OLD = listMsg[0]
NEW = ''
S = ''
C = ''
decodedMsg += decodeTable[OLD]

for i in range(1,len(listMsg)):
    NEW = listMsg[i]
    if decodeTable.get(NEW) == None:
        S = decodeTable[OLD]
        S = S + C
    else:
        S = decodeTable[NEW]
    decodedMsg += S
    C = S[0]
    decodeTable[str(decVal)] = chr(int(OLD)) + C
    decVal += 1
    OLD = NEW
print(decodedMsg)

