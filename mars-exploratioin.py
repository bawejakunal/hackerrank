#!/bin/python3

# https://www.hackerrank.com/challenges/mars-exploration

S = input().strip()
alt = 0
for i in range(0,len(S),3):
    if S[i] != 'S':
        alt += 1
    if S[i+1] != 'O':
        alt += 1
    if S[i+2] != 'S':
        alt += 1
print(alt)