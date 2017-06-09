#!/bin/python3

"""
https://www.hackerrank.com/challenges/the-birthday-bar
"""

import sys

def solve(n, s, d, m):
    ways = 0
    if n < m:
        ways = 0
    else:
        cs = sum(s[:m])
        for i in range(m-1, n):
            if i > m-1:
                cs = cs + s[i] - s[i-m]
            if cs == d:
                ways += 1
    return ways

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
