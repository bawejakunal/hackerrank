#!/bin/python
"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited
"""
import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
clouds = map(int,raw_input().strip().split(' '))

#n % k = 0 (given) => n is multiple of k
#so count 0th cloud at start of loop itself, this is
#safe because n >=2 so there will be no corner case
#where there is no jump, always at least 2 jumps

exhaust = 0
for i in xrange(0, n, k):
    exhaust += 1 + (2 * clouds[i])

print 100 - exhaust
