"""
https://www.hackerrank.com/challenges/waiter
"""

import math

def generate_primes(q):
    primes = list()
    num = 2
    while len(primes) < q:
        root = math.ceil(math.sqrt(num))
        i = 2
        while i <= root:
            if num % i == 0:
                break
            i += 1
        if i > root or num == 2:
            primes.append(num)
        num += 1
    return primes

def main():
    N, Q = map(int, input().split())
    B = list()
    B.append(list()) # B[0]
    A = list(map(int, input().split()))
    An = list()
    primes = generate_primes(Q)
    
    for i in range(Q):
        B.append(list())
        while len(A) > 0:
            if A[-1] % primes[i] == 0:
                B[i+1].append(A.pop())
            else:
                An.append(A.pop())
        A = list(An)
        An = list()
    for b in B[1:]:
        while len(b) > 0:
            print(b.pop())
    while len(A) > 0:
        print(A.pop())

if __name__ == '__main__':
    main()