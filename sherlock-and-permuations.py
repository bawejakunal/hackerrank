"""
https://www.hackerrank.com/challenges/sherlock-and-permutations/problem
"""

import math

def choose(n, k, mod=1):
    k = min(k, n-k)
    if k == 0:
        return 1
    choices = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
    choices %= mod
    return choices

t = int(input().strip())
while t > 0:
    n,m = list(map(int, input().split()))
    ans = choose(n+m-1, n, mod=1000000007)
    print(ans)
    t -= 1