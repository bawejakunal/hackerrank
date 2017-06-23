# https://www.hackerrank.com/challenges/grid-challenge/

def is_column_sorted(G, N):
    _sorted = True
    for col in range(N):
        for row in range(N-1):
            if G[row][col] > G[row+1][col]:
                _sorted = False
                break
        if _sorted is False:
            break
    return _sorted

def main():
    T = int(input().strip())
    while T > 0:
        N = int(input().strip())
        G = list()
        for i in range(N):
            G.append(list(input().strip())) # sort each row
            G[-1].sort()
        if is_column_sorted(G, N):
            print('YES')
        else:
            print('NO')
        T -= 1

if __name__ == '__main__':
    main()
