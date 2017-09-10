#! usr/bin/env python
#! coding:utf-8

import random
#生成随机整数，从0-99，但会重复
"""
word=[]
for i in range(7):
    for j in range(4):
        w = random.randint(0,99)
        word.append(w)

print(word)
"""
#生成不重复的0-99随机数
number_list=[]

for i in range(100):
    number_list.append(i)

word = random.sample(number_list,28)

print(word)
