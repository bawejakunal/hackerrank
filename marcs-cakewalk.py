#!/bin/python3

# https://www.hackerrank.com/challenges/marcs-cakewalk

n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
miles = 0
calories.sort(reverse=True)
for j in range(n):
    miles += (2**j) * calories[j]
print(miles)