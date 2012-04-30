#!/usr/bin/env python

answer = None
data1 = [1,2,3,4,5]
data2 = ['A', 'B', 'C', 'D', 'E']

answer = zip(data1, data2)

assert answer == [ (1,'A'), (2,'B'), (3,'C'), (4, 'D'),(5,'E') ]
