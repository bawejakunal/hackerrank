#!/bin/python3

# https://www.hackerrank.com/challenges/the-hurdle-race

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
# your code goes here
drinks = 0
for h in height:
    if h > k:
        diff = h - k
        k += diff
        drinks += diff
print(drinks)