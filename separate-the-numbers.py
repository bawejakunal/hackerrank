#!/bin/python3

# https://www.hackerrank.com/challenges/separate-the-numbers

import math

def __is_beautiful(number, string):
    if string == "":
        return True
    else:
        second = str(int(number) + 1)
        if string.startswith(second):
            return __is_beautiful(second, string[len(second):])
        else:
            return False

def is_beautiful(number):
    if len(number) > 1:
        for i in range(1, math.ceil(len(number)/2)+1):
            first = number[:i]
            if not first.startswith('0') and __is_beautiful(first, number[i:]):
                return first
    return None

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    x = is_beautiful(s)
    if x is not None:
        print("YES", x)
    else:
        print("NO")
