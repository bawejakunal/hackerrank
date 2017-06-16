#!/bin/python3

# https://www.hackerrank.com/challenges/string-construction

def stringConstruction(s):
    chars = set(s)
    return len(chars)

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = stringConstruction(s)
    print(result)
