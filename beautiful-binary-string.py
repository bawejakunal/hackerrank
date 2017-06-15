#!/bin/python3

# https://www.hackerrank.com/challenges/beautiful-binary-string

import sys

def minSteps(n, B):
    s = B
    count = 0
    for i in range(n-2):
        if s[i:i+3] == "010":
            s = s[:i+2] + "1" + s[i+3:]
            count += 1
    return count

n = int(input().strip())
B = input().strip()
result = minSteps(n, B)
print(result)
