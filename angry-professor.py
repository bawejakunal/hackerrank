#!/bin/python
"""
https://www.hackerrank.com/challenges/angry-professor
"""
import sys

t = int(raw_input().strip())
while t > 0:
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = map(int, raw_input().strip().split(' '))
    count = 0
    for time in a:
        if time <= 0:
            count += 1
    if count < k:
        print 'YES'
    else:
        print 'NO'
    t -= 1
