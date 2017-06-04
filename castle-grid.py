"""
https://www.hackerrank.com/challenges/castle-on-the-grid

Explanation below
"""

from collections import deque

def main():
    N = int(input())
    grid = list()
    dist = list()
    for _ in range(N):
        grid.append(input().strip())
        dist.append([N**2]*N)
    a, b, c, d = map(int, input().split())

    q = deque()

    dist[a][b] = 0
    q.append((a, b))

    while len(q) > 0:
        x, y = q.popleft()
        _mv = dist[x][y] + 1

        # upwards
        _x = x - 1
        while _x >= 0 and grid[_x][y] != 'X':
            if _mv < dist[_x][y]:
                dist[_x][y] = _mv
                q.append((_x, y))
            _x -= 1

        # left
        _y = y - 1
        while _y >= 0 and grid[x][_y] != 'X':
            if _mv < dist[x][_y]:
                dist[x][_y] = _mv
                q.append((x, _y))
            _y -= 1

        # down
        _x = x + 1
        while _x < N and grid[_x][y] != 'X':
            if _mv < dist[_x][y]:
                dist[_x][y] = _mv
                q.append((_x, y))
            _x += 1


        # right
        _y = y + 1
        while _y < N and grid[x][_y] != 'X':
            if _mv < dist[x][_y]:
                dist[x][_y] = _mv
                q.append((x, _y))
            _y += 1

    print(dist[c][d])


if __name__ == '__main__':
    main()


"""
This question simulates movements of a castle move in chess.
A move is movement in any one of possible 4 directions until an obstruction or
end of board or the desired destination point.

Start and end can be any locations within the given NxN grid
X - obstruction
. - allowed to move through

We need to calculate the minimum number of turns (moves) required to reach
destination.

Formulate this problem as a BFS shortest distance graph problem.
- A grid cell is a node in the graph.
- All the cells in a direction until a X or grid boundary can be reached in 
a single move. Hence distance between the given cell and those cells lying
in a straight line is considered to be 1 (1 more than the src-cell distance)

- if a src-cell distance is updated it is added back to the queue
"""