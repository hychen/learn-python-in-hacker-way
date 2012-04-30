#!/usr/bin/env python

answer = None
data = {'a':1, 'b':2, 'c':3, 'd':4}
tmp = []

keys = sorted(data.keys())
values = sorted(data.values())
for k, v in zip(keys, values):
	tmp.append('{0}={1}'.format(k, v))

answer = ', '.join(tmp)
assert answer == 'a=1, b=2, c=3, d=4', answer
