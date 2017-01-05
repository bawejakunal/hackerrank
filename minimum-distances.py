#!/bin/python
"""
https://www.hackerrank.com/challenges/minimum-distances
"""

def main():
    """
    minimum distance between equal elements
    """
    n = int(raw_input().strip())
    A = map(int, raw_input().strip().split(' '))

    distance = n #initialize, at most n-1 is possible
    for i in xrange(n):
        for j in xrange(i+1, min(n, i + distance)):
            if A[i] == A[j]:
                distance = j - i
                break

    if distance == n:
        distance = -1

    print distance

if __name__ == '__main__':
    main()
