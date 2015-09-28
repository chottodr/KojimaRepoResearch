#!/usr/bin/env python
# -*- coding: utf-8 -*-
#graph.py

import sys
import re
import numpy as np
import pylab as plt

argvs =sys.argv
path = argvs[1]

data = []
datas = []
document = []
doc = open(path,'r')
data = doc.read()
linesl = data.split("\n")
for line in linesl:
    document.append((line))
document.pop()

f = open(path+".tsv",'w')
for i in document:
    data = i.split(' + ')
    for j in data:
        f.write(j.split('*')[0])
        f.write("\t")
        f.write(j.split('*')[1])
        f.write("\n")
f.close()

g_data = np.genfromtxt(path+".tsv",delimiter="\t",dtype=[("data1",float),("data2","S512")])
print g_data[0][0]
for num in range(0,20):
    key = []
    value = []
    for i in range(0,10):
        key.append(g_data[num*10+i][0])
        value.append(g_data[num*10+i][1])
    print key
    print value
    X=[1,2,3,4,5,6,7,8,9,10]
    plt.barh(X,key, height=0.4,align="center")  # 中央寄せ
    plt.yticks(X, value)
    plt.show()

