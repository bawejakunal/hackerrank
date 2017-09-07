#!/bin/python3
"""
https://www.hackerrank.com/challenges/knightl-on-chessboard
"""

from collections import deque

class KnightL(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def isValidCell(self, n, cell):
        return (0 <= cell[0] < n) and (0 <= cell[1] < n)
    
    def addNeighbors(self, q, board, cell):
        r = cell[0]
        c = cell[1]
        a = self.a
        b = self.b

        neighbors = set([(r-a,c-b),(r-a,c+b),(r+a,c-b),(r+a, c+b)])
        if a != b:
            a, b = b, a
            neighbors.update([(r-a,c-b),(r-a,c+b),(r+a,c-b),(r-a,c+b),(r+a,c+b)])

        for nbr in neighbors:
            if self.isValidCell(len(board), nbr):
                if board[nbr[0]][nbr[1]] == -1:
                    q.append(nbr)
                    board[nbr[0]][nbr[1]] = board[r][c] + 1
    
    def leastMoves(self, n):
        board = [[-1 for i in range(n)] for j in range(n)]
        board[0][0] = 0
        q = deque()
        q.append((0, 0))
        
        while len(q) > 0:
            cell = q.popleft()
            if cell[0] == n-1 == cell[1]:
                break
            self.addNeighbors(q, board, cell)
        
        return board[n-1][n-1]
            
        


def main():
    n = int(input().strip())
    for a in range(1, n):
        for b in range(1, n):
            knight = KnightL(a, b)
            print(knight.leastMoves(n), end=' ')
        print()

if __name__ == '__main__':
    main()
