#!/bin/python
"""
https://www.hackerrank.com/challenges/cavity-map
"""

def is_cavity(grid, r, c):
    """
    check cavity satisfying conditions
    """
    result = True
    result = result and grid[r][c] > grid[r-1][c]
    result = result and grid[r][c] > grid[r][c-1]
    result = result and grid[r][c] > grid[r+1][c]
    result = result and grid[r][c] > grid[r][c+1]
    return result

def main():
    n = int(raw_input().strip())
    grid = list()
    for _ in xrange(n):
        grid_t = raw_input().strip()
        grid.append(grid_t)

    for i in xrange(1, n-1):
        for j in xrange(1, n-1):
            if is_cavity(grid, i, j):
                grid[i] = grid[i][:j] + 'X' + grid[i][j+1:]

    for row in grid:
        print row

if __name__ == '__main__':
    main()
