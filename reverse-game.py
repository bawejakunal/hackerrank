#!/bin/python3

# https://www.hackerrank.com/challenges/reverse-game/problem

t = int(input().strip())
while t > 0:
    n, k = list(map(int, input().strip().split(' ')))
    if k < n // 2:
        k = (2 * k) + 1
    else:
        k = (n - 1 - k) * 2 
    print(k)
    t -= 1