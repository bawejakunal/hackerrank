#!/bin/python
"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds
"""
import sys

n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

jumps = 0
i = 0
while i < n - 1:
    if i == n-2 or c[i+2] == 1:
        i += 1
    else:
        i += 2
    jumps += 1

print jumps
