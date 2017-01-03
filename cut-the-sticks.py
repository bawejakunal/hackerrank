#!/bin/python
"""
https://www.hackerrank.com/challenges/cut-the-sticks
"""

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

arr.sort(reverse=True)
while len(arr) > 0:
    print len(arr) #all sticks are cut
    arr = map(lambda x: x - arr[-1], arr)
    while len(arr) > 0 and arr[-1] == 0:
        arr.pop()
