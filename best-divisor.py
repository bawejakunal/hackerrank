# https://www.hackerrank.com/challenges/best-divisor

#!/bin/python3

import sys

def get_divisors(n):
    num = n
    divs = set()
    for p in range(1, int(pow(num, 0.5)) + 1):
        if 0 == num % p:
            divs.add(p)
            divs.add(num//p)
    return divs

def digisum(n):
    num = n
    _sum = 0
    while num > 0:
        _sum += num % 10
        num //= 10
    return _sum
            
n = int(input().strip())
divs = get_divisors(n)
best = 1
bestsum = 1
while len(divs) > 0:
    d = divs.pop()
    dsum = digisum(d)
    if dsum > bestsum:
        bestsum = dsum
        best = d
    elif dsum == bestsum:
        best = min(best, d)
print(best)