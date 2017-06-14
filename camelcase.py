#!/bin/python3

# https://www.hackerrank.com/challenges/camelcase

s = input().strip()
count = 1
for ch in s:
    if ord(ch) <= 90:
        count += 1
print(count)
