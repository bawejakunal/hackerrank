#!/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

from collections import Counter

def sherlockAndAnagrams(s):
    count = 0
    tbl = dict()
    # substring starts at i
    for i in range(0, len(s)):
        # substring ends at j-1
        for j in range(i+1, len(s)+1):
            chars = list(s[i:j])
            chars.sort()
            t = "".join(chars)
            tbl[t] = tbl.get(t, 0) + 1
    for val in tbl.values():
        count += val*(val-1)//2
    return count

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = sherlockAndAnagrams(s)
    print(result)
