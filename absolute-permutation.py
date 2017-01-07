#!/bin/python
"""
https://www.hackerrank.com/challenges/absolute-permutation
"""

t = int(raw_input().strip())
for _ in xrange(t):
    n, k = map(int, raw_input().strip().split(' '))

    #special case of k = 0, generates smallest permutation
    if k == 0:
        print " ".join(map(str, range(1, n+1)))

    #not possible to swap in k sized subsets
    elif n % k > 0 or (n / k) % 2 == 1:
        print -1

    else:
        permute = range(1, n+1)
        i = 0
        while i < n - k:
            permute[i], permute[i + k] = permute[i + k], permute[i]
            if (i + 1) % k == 0:
                i += k + 1
            else:
                i += 1

        print " ".join(map(str, permute))
