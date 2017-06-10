#!/bin/python3

# https://www.hackerrank.com/challenges/picking-numbers

import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
counts = [0] * 100
maxcnt = 0
for num in a:
    counts[num] += 1
for i in range(1, 99):
    s = counts[i] + counts[i+1]
    if s > maxcnt:
        maxcnt = s
print(maxcnt)