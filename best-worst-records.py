#!/bin/python3

"""
https://www.hackerrank.com/challenges/breaking-best-and-worst-records
"""

import sys

def getRecord(scores):
    min_recs = 0
    max_recs = 0
    if len(scores) > 1:
        min_score = scores[0]
        max_score = scores[0]
        for i in range(1, len(scores)):
            if scores[i] < min_score:
                min_recs += 1
                min_score = scores[i]
            elif scores[i] > max_score:
                max_recs += 1
                max_score = scores[i]
    return max_recs, min_recs

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
