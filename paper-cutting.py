# https://www.hackerrank.com/challenges/p1-paper-cutting/

#!/bin/python3

import sys

def solve(n, m):
    # Complete this function
    return n * m - 1

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
result = solve(n, m)
print(result)
