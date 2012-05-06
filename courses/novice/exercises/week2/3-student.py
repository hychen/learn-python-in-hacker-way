#!/usr/bin/env python
# -*- coding: utf-8 -*-
# data 是一個包含整數1到500的list, 寫一個程式把總和算出來
# Note: 不可以使用`sum` function.
answer = 0
data = range(1,501)

# answer = ((data[0] + data[-1]) * len(data)) / 2
    
#for i in range(len(data)):
#    answer = answer + data[i]

# add all numbers in a list
# first check if input is valid, if so, print error, if not
# second check if all elements in the list are numbers, if so, add them up one by one and at the end return the sum; if not, report error

def func1(l=[], s=0):
    try:
	for x in l:
	    if not isinstance(x, int):
	        print "At lease one of the elements in the list is not a number."
	        break
            else:
	        s = s + x
        return s
    except TypeError as error:
	print error

answer = func1(data) 

assert answer == 125250, answer
