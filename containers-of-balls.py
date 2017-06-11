#!/bin/python3

# https://www.hackerrank.com/challenges/organizing-containers-of-balls

def colsum(mtrx, col):
    c_sum = 0
    for row in range(len(mtrx)):
        c_sum += mtrx[row][col]
    return c_sum

q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    for M_i in range(n):
        M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
        M.append(M_t)
    buckets = [sum(M[row]) for row in range(n)] # total balls in each bucket
    balls = [colsum(M, col) for col in range(n)] # total of each kind of ball
    
    possible = "Possible"
    # for each bucket
    for i in range(n):
        # for each type of ball from i to n-1
        j = i
        while j < n:
            if buckets[i] == balls[j]:
                balls[i], balls[j] = balls[j], balls[i]
                break
            j += 1
        if j == n:
            possible = 'Impossible'
            break
    print(possible)
    
