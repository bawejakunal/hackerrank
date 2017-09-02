"""
https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid
"""

from collections import deque

def isValidCell(grid, r, c):
    return not (r < 0 or r >= len(grid)
                or c < 0 or c >= len(grid[r])
                or grid[r][c] != 1)

def dfsGetSize(grid, r, c):
    if not isValidCell(grid, r, c):
        return 0
    s = 1
    grid[r][c] = -1     # mark visited
    for y in range(r-1, r+2):
        for x in range(c-1, c+2):
            s += dfsGetSize(grid, y, x)
    return s

def bfsGetSize(grid, r, c):
    if not isValidCell(grid, r, c):
        return 0
    
    q = deque()
    s = 0
    
    grid[r][c] = -1
    q.append((r, c))
    while len(q) > 0:
        y, x = q.popleft()
        s += 1    
        # add neigbors to queue
        for _y in range(y-1, y+2):
            for _x in range(x-1, x+2):
                if isValidCell(grid, _y, _x):
                    grid[_y][_x] = -1
                    q.append((_y, _x))
    return s

def getBiggestRegion(grid):
    bigr = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                bigr = max(bigr, dfsGetSize(grid, r, c))
    return bigr

def main():
    n = int(input().strip())
    m = int(input().strip())
    grid = []
    for grid_i in range(n):
        grid_t = list(map(int, input().strip().split(' ')))
        grid.append(grid_t)
    print(getBiggestRegion(grid))

if __name__ == '__main__':
    main()
