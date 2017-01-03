#!/bin/python

import sys

s = raw_input().strip()
n = long(raw_input().strip())

count = 0
length = len(s)

_a_in_str = 0
remainder = n % length

"""
Clever: traverse string only once
"""
for i in xrange(length):
    if s[i] == 'a':
        _a_in_str += 1
    #partial repition of s in n characters
    if (i + 1) == remainder:
        count += _a_in_str

#s has been repeated whole number of times
count += _a_in_str * (n / length)

print count
