#! /usr/bin/env python
# -*- coding: utf8 -*-

str1 = u'  《五音集韻》說：「人死為鬼，人見懼之；鬼死為魙，鬼見怕之。」  '
msg1 = str1.lstrip() # both type of str1 and msg1 is unicode
encoded1 = msg1.encode('utf8') # type of encoded1 is str
encoded1_part1 = encoded1[:39]
encoded1_part2 = encoded1[39:]
print encoded1_part1 + 'A' + encoded1_part2 # print str




