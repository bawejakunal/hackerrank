#!/bin/python3

# https://www.hackerrank.com/challenges/climbing-the-leaderboard

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

board = [scores[0]]
for score in scores[1:]:
    if board[-1] != score:
        board.append(score)

rank = len(board) + 1
for i in range(m):
    while rank > 1 and board[rank-2] <= alice[i]:
        rank -= 1
    print(rank)