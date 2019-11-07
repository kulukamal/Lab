import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import queue

class Node:
    def __init__(self, c1, c2, code, prob):
        self.c1 = c1
        self.c2 = c2
        self.code = code
        self.prob = prob
    def prt(self):
        print(self.prob)
        print(self.c1,self.c2,self.code)
        print('------------')

def huffManCoding(listOfData, listOfProb) :
    List = []
    posList = []
    for i in range(len(listOfData)):
        tmp = Node(-1, -1,'',listOfProb[i])
        List.append(tmp)
    prob = 0
    lAvg = 0
    H = 0
    eff = 0
    root = -1
    while prob < 1:
        low1 = 1
        low2 = 1
        pos1 = -1
        pos2 = -1

        for i in range(len(List)):
            if posList.__contains__(i):
                continue
            if List[i].prob < low1 :
                low2 = low1
                pos2 = pos1
                low1 = List[i].prob
                pos1 = i
            else :
                if List[i].prob < low2:
                    low2 = List[i].prob
                    pos2 = i
        
        tmp = Node(pos1, pos2,'',low1 + low2)
        posList.append(pos1)
        posList.append(pos2)
        prob = np.maximum(prob, tmp.prob)
        List.append(tmp)
        root = len(List) - 1
    cnt = len(List) - 1
    q = queue.Queue()
    q.put(root)
    while not(q.empty()):
        u = q.get()
        if List[u].c1 != -1:
            l = List[u].c1
            r = List[u].c2
            List[l].code = List[u].code + '0'
            List[r].code = List[u].code + '1'
            q.put(l)
            q.put(r)
        else :
             print(listOfData[u],List[u].code)
             lAvg += listOfProb[u] * len(List[u].code)
             H += listOfProb[u] * np.log2(1/listOfProb[u])
    print('Lavg = ',lAvg)
    print('Entropy = ',H)
    print('Efficency = ',H/lAvg)
    
 


huffManCoding([1,2,3,4], [0.1,0.2,0.3,0.4])
            
    