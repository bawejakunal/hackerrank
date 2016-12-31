#!/bin/python
"""
https://www.hackerrank.com/challenges/apple-and-orange
"""

import sys

s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apples = map(int,raw_input().strip().split(' '))
oranges = map(int,raw_input().strip().split(' '))

count_apple = count_orange = 0
for apple in apples:
    position = a + apple
    if s <= position <= t:
        count_apple += 1

for orange in oranges:
    position = b + orange
    if s <= position <= t:
        count_orange += 1

print count_apple
print count_orange
