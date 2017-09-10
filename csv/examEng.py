#! usr/bin/env python
#! coding:utf-8
import pandas as pd
import numpy as np
import csv
import random

count = 200.0

csvfile = pd.read_csv('engishword.csv')


idx=[]
csvfile_size = len(csvfile)
for i in range(csvfile_size):
    idx.append(i)

random.shuffle(idx)
cnt=0

wronglist = []
answer = []

for i in range(int(count)):
    print("The" + " " + str(i+1) + " " + "word.")
    print csvfile.loc[idx[i]]["chinese"]
    word = raw_input("your input:")
    print csvfile.loc[idx[i]]["english"]
    if word == csvfile.loc[idx[i]]["english"]:
        cnt = cnt + 1
        print("correct!")
    else:
        print('\033[1;31;40m')
        print("incorrect!")
        print('\033[0m')
        wronglist.append(word)
        answer.append(csvfile.loc[idx[i]]["english"])
accuracy = (cnt / count) * 100
print("正确率：" + str(accuracy) + "%")
print(wronglist)
print(answer)
