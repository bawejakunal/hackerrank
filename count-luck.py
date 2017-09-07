"""
https://www.hackerrank.com/challenges/count-luck
"""

def get_input():
    N, M = list(map(int, input().split()))
    forest = list()
    start = None
    end = None
    for i in range(N):
        row = list(input().strip())
        if 'M' in row:
            start = (i, row.index('M'))
        if '*' in row:
            end = (i, row.index('*'))
        forest.append(row)
    
    K = int(input().strip())
    return N, M, forest, start, end, K

def isValidCell(forest, cell, N, M):
    return ((0 <= cell[0] < N) and
            (0 <= cell[1] < M) and
            (forest[cell[0]][cell[1]] != 'X'))

def getValidNeighbors(forest, N, M, cell):
    neighbors = list()
    nbr = (cell[0], cell[1] - 1)
    if isValidCell(forest, nbr, N, M):
        neighbors.append(nbr)
    
    nbr = (cell[0], cell[1] + 1)
    if isValidCell(forest, nbr, N, M):
        neighbors.append(nbr)
    
    nbr = (cell[0] - 1, cell[1])
    if isValidCell(forest, nbr, N, M):
        neighbors.append(nbr)
    
    nbr = (cell[0] + 1, cell[1])
    if isValidCell(forest, nbr, N, M):
        neighbors.append(nbr)
    
    return neighbors

def isImpressed(N, M, forest, current, end, K):
    # reached end in exact waves
    if current == end:
        return K == 0

    forest[current[0]][current[1]] = 'X'    # block this cell as visited
    neighbors = getValidNeighbors(forest, N, M, current)
    if len(neighbors) == 1:
        return isImpressed(N, M, forest, neighbors[0], end, K)  # no waving
    
    for nbr in neighbors:
        if isImpressed(N, M, forest, nbr, end, K - 1):   # waved here
            return True
    return False

def main():
    T = int(input().strip())
    while T > 0:
        N, M, forest, start, end, K = get_input()
        print('Impressed' if isImpressed(N, M, forest, start, end, K) else 'Oops!')
        T -= 1

if __name__ == '__main__':
    main()
