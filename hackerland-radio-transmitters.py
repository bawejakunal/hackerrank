"""
https://www.hackerrank.com/challenges/hackerland-radio-transmitters
"""

#!/bin/python3

import sys

def findTransmitters(arr, dist):
    idx = 0
    total = 0
    while idx < len(arr):
        mid = arr[idx] + dist
        while idx < len(arr) and arr[idx] <= mid:
            idx += 1
        total += 1 # place transmitter at mid
        
        idx -= 1    # middle house
        end = arr[idx] + dist
        while idx < len(arr) and arr[idx] <= end:
            idx += 1
    
    return total
        
    

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]
x.sort()
print(findTransmitters(x, k))