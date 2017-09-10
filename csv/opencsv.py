#! usr/bin/env python
#! coding:utf-8
import numpy as np
import csv
import random

csvfile = open('engishword.csv','r')
data = [] 
indx = []
for line in csvfile:
    data.append(list(line.strip().split(',')))

for i in range(len(data)):
    indx.append(i)
random.shuffle(indx)

#print(indx)

for i in range(100):
    print(data[indx[i]])

#=====================
#=====直接打乱========
#=====================
#random.shuffle(data)
#print(data)
