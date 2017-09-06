"""
https://www.hackerrank.com/challenges/big-sorting
"""

#!/bin/python3

def sortStrings(unsorted):
    unsorted.sort(key=len)
    start = 0
    idx = start
    while idx < len(unsorted):
        while (idx < len(unsorted) and
               len(unsorted[start]) == len(unsorted[idx])):
            idx += 1
        end = idx
        _sorted = sorted(unsorted[start:end])
        for i in range(len(_sorted)):
            unsorted[start+i] = _sorted[i]
        start = end
    

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)
# your code goes here
sortStrings(unsorted)
for s in unsorted:
    print(s)