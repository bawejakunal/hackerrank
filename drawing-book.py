#!/bin/python3

# https://www.hackerrank.com/challenges/drawing-book

import math

def solve(n, p):
    turns = None
    # front
    turns = p // 2
    # back
    if p % 2 == 0:
        p += 1
    turns = min(turns, math.ceil((n - p)/2))
    return turns

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
