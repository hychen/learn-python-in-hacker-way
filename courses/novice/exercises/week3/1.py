#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# 現有兩陣列 A, B，請撰寫ㄧFunction 名叫*uniq_merge*, 功用為能將兩個陣列合併，並去除重複的字串或數字
#
# Input: 兩個一維陣列
# Output: 一個一維陣列
A = ['been', 'for', 'posting', 7, 'looking', 1, 'and', 'this!', 5, 0, 'a', 'Xmonad', 'uses', 'replacement', 'might', 'ratpoison', 'it.', 2, 'Ubuntu', 8, 3, 'Dvorak', 'Thanks', 'for', 6, 'be', 'who', 'here.', 4, "I've", 'typist']
B = [1, 11, 'typist', 'Dvorak', 'it.', 9, 'be', 'for', 'a', 'uses', 'posting', 'looking', 4, 6, 'this!', 10, 'Xmonad', 'replacement', 13, 'ratpoison', 'who', 8, 0, 'Ubuntu', 'might', 'a', 7, "I've", 'and', 3, 5, 'for', 'been', 'Thanks', 12, 'here.', 2, 'a']

def uniq_merge(a,b):
    pass

excepted = ['and', 1, 2, 3, 4, 5, 0, 7, 8, 9, 10, 11, 12, 13, 'Xmonad', 6, 'for', "I've", 'been', 'looking', 'Ubuntu', 'Dvorak', 'might', 'here.', 'it.', 'a', 'posting', 'who', 'uses', 'be', 'this!', 'Thanks', 'typist', 'ratpoison', 'replacement']
assert excepted == uniq_merge(A,B)
