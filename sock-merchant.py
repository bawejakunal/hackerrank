#!/bin/python
"""
https://www.hackerrank.com/challenges/sock-merchant
"""
import sys

n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

d =  dict()
pair = 0
for sock in c:
    if sock in d:
        d[sock] += 1
    else:
        d[sock] = 1

for colour in d:
    pair += d[colour] / 2

print pair
