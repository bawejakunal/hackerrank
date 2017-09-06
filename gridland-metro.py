"""
https://www.hackerrank.com/challenges/gridland-metro
"""

def main():
    n, m, k = list(map(int, input().split()))
    tracks = dict()
    occupied = 0
    for i in range(k):
        r, c1, c2 = list(map(int, input().split()))
        if r in tracks:
            tracks[r].append((c1, c2))
        else:
            tracks[r] = [(c1, c2)]
     
    for r in tracks:
        row = tracks[r]
        row.sort()
        start = row[0][0]
        end = row[0][1]
        for i in range(1, len(row)):
            if row[i][0] > end:
                occupied += end - start + 1
                start, end = row[i]
            else:
                end = max(row[i][1], end)
        occupied += end - start + 1

    print((n * m) - occupied)

if __name__ == '__main__':
    main()