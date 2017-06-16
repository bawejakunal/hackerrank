#!/bin/python3

# https://www.hackerrank.com/challenges/two-strings

def twoStrings(s1, s2):
    char1 = set(s1)    
    char2 = set(s2)
    return 'NO' if char1.isdisjoint(char2) else 'YES'

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
