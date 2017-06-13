#!/bin/python3

# https://www.hackerrank.com/challenges/weighted-uniform-string

s = input().strip()
n = int(input().strip())
w = set()
i = 0
while i < len(s):
    cw = ord(s[i])-96 # cumulative weight
    w.add(cw)
    j = i+1
    wt = cw
    while j < len(s) and s[j] == s[i]:
        cw += wt
        w.add(cw)
        j += 1
    i = j
for a0 in range(n):
    x = int(input().strip())
    # your code goes here
    if x in w:
        print('Yes')
    else:
        print('No')
