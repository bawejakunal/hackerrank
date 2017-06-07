#!/bin/python3

"""
https://www.hackerrank.com/challenges/hackerrank-in-a-string
"""

def subseq(ptrn, dest):
    i = 0
    j = 0
    while j < len(dest) and i < len(ptrn):
        if dest[j] == ptrn[i]:
            i += 1
        j += 1
    return (i == len(ptrn)) and (j <= len(dest))

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    if subseq("hackerrank", s):
        print('YES')
    else:
        print('NO')

# search a subsequence in a string
