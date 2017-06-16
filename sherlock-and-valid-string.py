#!/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

def isValid(s):
    chars = dict()
    for ch in s:
        chars[ch] = chars.get(ch, 0) + 1
    vals = list(chars.values())
    counts = dict()
    for val in vals:
        counts[val] = counts.get(val,0) + 1
    # more than 2 chars
    if len(counts) > 2:
        return 'NO'
    # only 1 char or out of 2 differing chars one has count == 1
    elif len(counts) == 1 or min(counts.values()) == 1:
        return 'YES'
    # other cases
    return 'NO'

s = input().strip()
result = isValid(s)
print(result)
