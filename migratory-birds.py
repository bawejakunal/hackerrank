#!/bin/python3

# https://www.hackerrank.com/challenges/migratory-birds

import sys

def migratoryBirds(n, ar):
    counts = [0, 0, 0, 0, 0]
    for i in range(n):
        counts[ar[i]-1] += 1
    mx, idx = counts[0], 0
    for i in range(1,5):
        if counts[i] > mx:
            mx = counts[i]
            idx = i
    return idx + 1

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
