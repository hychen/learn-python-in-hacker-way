#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 想出方法不使用 if..else 重寫ask_it來達成同樣的功能
#

def answer_yes(name):
    print 'YES, ' + name

def answer_no(name):
    print 'NO, ' + name

ret = raw_input('yes or no?')

def ask_it(ret):
    if ret == 'yes':
        answer_yes('My Lord')
    elif ret == 'no':
        answer_no('man')

ask_it(ret)
