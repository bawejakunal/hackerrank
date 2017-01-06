#!/bin/python
"""
https://www.hackerrank.com/challenges/fair-rations
"""

N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))

bread = 0
for i in xrange(N):
    if i == N - 1 and B[i] % 2 != B[i - 1] % 2:
        bread = -1
        break

    elif B[i] % 2 == 1:
        B[i] += 1
        B[i + 1] += 1 
        bread += 2

if bread == -1:
    print 'NO'
else:
    print bread
