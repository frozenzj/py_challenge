# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:03:50 2019

@author: zj
"""

a = [1, 11, 21, 1211, 111221]
b=['1',]
for i in range(30):
    text=b[i]
    output=''   
    num_count=1
    for x in text[1:]:
        if x==text[0]:
            num_count+=1
            text=text[1:]
        else:
            output+=str(num_count)+text[0]
            text=text[1:]
            num_count=1
    output+=str(num_count)+text[0]
    b.append(output)