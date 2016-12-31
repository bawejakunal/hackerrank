#!/bin/python
"""
https://www.hackerrank.com/challenges/divisible-sum-pairs
"""

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))

count = 0
for i in xrange(n-1):
    for j in xrange(i+1, n):
        count += 1 if (a[i] + a[j]) % k == 0 else 0

print count
