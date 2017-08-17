#!/bin/python3

# https://www.hackerrank.com/challenges/ctci-find-the-running-median

import sys
from heapq import *

n = int(input().strip())
minheap = list()
maxheap = list()
median = 0
for i in range(1, n+1):
    t = int(input().strip())
    if t > median:
        heappush(minheap, t)
    else:
        heappush(maxheap, -t)
    while len(maxheap) > (len(minheap) + 1):
        heappush(minheap, -heappop(maxheap))
    while len(minheap) > len(maxheap):
        heappush(maxheap, -heappop(minheap))
    if ((i & 1) == 1):
        median = float(-maxheap[0])
    else:
        median = (minheap[0] - maxheap[0]) / 2
    print("%.1f" % median)
