#!/usr/bin/env python
# 將 data1 與 data2 合併成為一個陣列, 合併規則為
# [ (data1 第一個元素, data2 第一個元素), (data1 第二個元素, data2 第二個元素), .... ]
answer = None
data1 = [1,2,3,4,5]
data2 = ['A', 'B', 'C', 'D', 'E']
assert answer == [ (1,'A'), (2,'B'), (3,'C'), (4, 'D'),(5,'E') ]
