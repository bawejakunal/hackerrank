#!/bin/python3

# https://www.hackerrank.com/challenges/cats-and-a-mouse

import sys

q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    diff = abs(z-x) - abs(z-y)
    if diff < 0:
        print('Cat A')
    elif diff == 0:
        print('Mouse C')
    else:
        print('Cat B')
