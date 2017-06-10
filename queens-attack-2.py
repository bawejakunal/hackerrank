#!/bin/python3

# https://www.hackerrank.com/challenges/queens-attack-2

def is_on_path(queen, obs):
    direction = 0

    # same row
    if queen[0] == obs[0]:
        direction = 1 if obs[1] > queen[1] else 5
    # same column
    elif (queen[1] == obs[1]):
        direction = 3 if obs[0] > queen[0] else 7
    # diagonals
    elif (abs(queen[0]-obs[0]) == abs(queen[1]-obs[1])):
        # upper
        if obs[0] > queen[0]:
            # right
            direction = 2 if obs[1] > queen[1] else 4
        # lower
        else:
            direction = 8 if obs[1] > queen[1] else 6
    return direction

def queen_squares(n, q, blkd):
    # max squares queen can attack in all directions
    sqrs = 0
    for d in range(1, 9):
        if d in blkd:
            sqrs += blkd[d][1] # 2nd of tuple is distance
        else:
            if d == 1:
                sqrs += n - q[1]
            elif d == 2:
                sqrs += min(n-q[0], n-q[1]) # right upper diagonal
            elif d == 3:
                sqrs += n - q[0]
            elif d == 4:
                sqrs += min(n-q[0], q[1]-1) # left upper diagonal
            elif d == 5:
                sqrs += q[1] - 1
            elif d == 6:
                sqrs += min(q[0]-1, q[1]-1) # left lower diagonal
            elif d == 7:
                sqrs += q[0]-1
            elif d == 8:
                sqrs += min(q[0]-1, n-q[1]) # right lower diagnonal
    return sqrs

def distance(q, p):
    return max(abs(q[0]-p[0]), abs(q[1]-p[1]))

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]

blkd_sqrs = dict()
for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    # your code goes here
    direction = is_on_path((rQueen, cQueen),(rObstacle, cObstacle))
    dist = distance((rQueen, cQueen),(rObstacle, cObstacle)) - 1
    
    # on path
    if direction > 0:
        if direction in blkd_sqrs:
            if blkd_sqrs[direction][1] > dist:
                blkd_sqrs[direction] = ((rObstacle, cObstacle), dist)
        else:
            blkd_sqrs[direction] = ((rObstacle, cObstacle), dist)

print(queen_squares(n, (rQueen, cQueen), blkd_sqrs))