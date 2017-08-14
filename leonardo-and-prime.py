"""
https://www.hackerrank.com/challenges/leonardo-and-prime/problem
"""

import bisect
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
it = 1
prods = []
for i in primes:
    it *= i
    prods.append(it)
for i in range(int(input())):
    t = bisect.bisect(prods, int(input()))
    print(t)
