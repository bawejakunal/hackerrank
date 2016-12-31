#!/bin/python
"""
https://www.hackerrank.com/challenges/between-two-sets
"""

"""
x is divisible by all numbers of a iff it is divisible by their least common
multiple. Denote it as L.

All numbers of b are divisible by x iff the greatest common divisor of all
numbers of b is divisible by x. Denote it as G.
"""

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

def gcd(first, second):
    """
    Greatest Common Divisor
    """
    if first < second:
        return gcd(second, first)
    while second > 0:
        first, second = second, first % second
    return first

def lcm(first, second):
    """
    LCM of two numbers
    LCM * GCD = First * Second
    """
    return (first / gcd(first, second)) * second

count = 0

#LCM of all numbers in set a
L = 1
for i in a:
    L = lcm(i, L)

#GCD of all numbers in set b
G = 0
for i in b:
    G = gcd(i, G)

"""
x should be common multiple of all numbers in set a and
common divisor of all numbers in set b, thus GCD of b should
be divisble by LCM of a, else no value of x can be found
"""
if G % L != 0:
    count = 0

else:
    for i in xrange(L, G+1):
        if (G % i == 0) and (i % L == 0):
            count += 1

print count
