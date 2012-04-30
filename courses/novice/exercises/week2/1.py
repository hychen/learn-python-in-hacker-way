#!/usr/bin/env python
answer = None
data = [ [1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15] ]

tmp = data[0] + data[1]
tmp.append('A')
answer = tmp + data[2]

assert answer == [1,2,3,4,5,6,7,8, 9,10, 'A', 11,12,13,14,15], answer
