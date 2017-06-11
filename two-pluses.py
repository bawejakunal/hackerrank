# https://www.hackerrank.com/challenges/two-pluses

def get_maxarea(grid, N, M, row, col):
    # arm length including center square
    arm = 1
    u, l, r, d = 1, 1, 1, 1

    # upper side
    while (row - u) >= 0 and grid[row - u][col] == grid[row][col]:
        u += 1
    arm = u
    # left side
    while (col - l) >= 0 and l < arm and grid[row][col - l] == grid[row][col]:
        l += 1
    arm = min(arm, l)
    # down side
    while (row + d) < N and d < arm and grid[row + d][col] == grid[row][col]:
        d += 1
    arm = min(arm, d)
    # right side
    while (col + r) < M and r < arm and grid[row][col + r] == grid[row][col]:
        r += 1
    arm = min(arm, r)
    size = arm * 4 - 3 # subtract 3 to reduce overcounting centre square
    return size

def intersects(first, second):
    arm1 = (first[1] + 3) // 4
    arm2 = (second[1] + 3) // 4
    hor = abs(first[0][1] - second[0][1]) + 1 # count of horizontal squares
    vert = abs(first[0][0] - second[0][0]) + 1 # count of vertical squares
    
    # same column
    if hor == 1:
        return  vert < arm1 + arm2
    # same row
    elif vert == 1:
        return  hor < arm1 + arm2
    # otherwise
    else:
        intersect = hor <= max(arm1, arm2) and vert <= min(arm1, arm2)
        intersect = intersect or \
                    (vert <= max(arm1, arm2) and hor <= min(arm1, arm2))
        return intersect

def main():
    """
    main method
    """
    N, M = map(int, input().strip().split())
    grid = list()
    for i in range(N):
        grid.append(input().strip())

    # list of all pluses
    plus = list()

    # for each grid square that can be a center of a plus
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'G':
                # area of largest plus around grid[i][j]
                maxarea = get_maxarea(grid, N, M, i, j)
                # count smaller pluses too
                # subsequent squares differ in area by 4
                for area in range(1, maxarea + 1, 4):
                    plus.append(((i, j), area))

    # for all pairs of non-overlapping squares
    maxprod = 0
    for i in range(len(plus) - 1):
        for j in range(i + 1, len(plus)):
            if not intersects(plus[i], plus[j]):
                temp = plus[i][1] * plus[j][1]
                if temp > maxprod:
                    maxprod = temp
    print(maxprod)

if __name__ == '__main__':
    main()