#! usr/bin/env python
#! coding:utf-8
import pandas as pd
import numpy as np
import csv
import random

count = 19.0

csvfile = pd.read_csv('sym_asym.csv')


idx=[]
csvfile_size = len(csvfile)
for i in range(csvfile_size):
    idx.append(i)

random.shuffle(idx)
cnt=0

for i in range(int(count)):
    print("The" + " " + str(i+1) + " " + "word.")
    word = csvfile.loc[idx[i]]
    notnulllist = csvfile.loc[idx[i]].notnull()
    #转化为list，可以不用
    #notnulllist = list(notnulllist)
    
    #判断该行（单词）是否有两个或以上同义词（判断size，个数？）
    #随机选择原词或者同义词显示
    truecnt = sum(notnulllist)
    j = random.randint(0,truecnt-1)
    print word[j]

    #等待输入
    input_word = raw_input("your input:")
    #输出正确答案列表，然后判断对错
    print list(word)
    k = 0
    match = 0
    while(k < truecnt):
        if(input_word == word[k]):
            match = 1
            cnt = cnt + 1
            print('\033[1;32;40m correct! \033[0m')
            break
        k = k + 1
    if (match == 0):
        print('\033[1;31;40m incorrect! \033[0m')

"""
    for k in range(int(truecnt)):
        if input_word == word[k]:
            cnt = cnt + 1
            print ("correct!")
        else:
            print("incorrect!")
"""
#打印正确率和正确答案
accuracy = (cnt / count) * 100
print("正确率：" + str(accuracy) + "%")
