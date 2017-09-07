"""
https://www.hackerrank.com/challenges/connected-cell-in-a-grid
"""

def isValid(n, m, r, c):
    return (0 <= r < n) and (0 <= c < m)

def dfsSize(board, n, m, r, c):
    if board[r][c] != 1:
        return 0
    
    size = 1
    board[r][c] = -1
    for row in range(r-1, r+2):
        for col in range(c-1, c+2):
            if isValid(n, m, row, col):
                size += dfsSize(board, n, m, row, col)
    return size

def largestIsland(board, rows, cols):
    largest = 0
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:
                size = dfsSize(board, rows, cols, r, c)
                largest = max(largest, size)
    return largest

def main():
    n = int(input().strip())
    m = int(input().strip())
    board = list()
    for r in range(n):
        board.append(list(map(int, input().split())))
    print(largestIsland(board, n, m))

if __name__ == '__main__':
    main()