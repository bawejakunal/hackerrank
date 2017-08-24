# https://www.hackerrank.com/challenges/most-distant/problem

def dist(a, b):
    d = (a[0]-b[0])**2 + (a[1]-b[1])**2
    d = pow(d, 0.5)
    return d

def main():
    n = int(input().strip())
    high = None
    low = None
    left = None
    right = None
    for i in range(n):
        a = list(map(int, input().split()))
        if high is None or high[1] < a[1]:
            high = a
        if low is None or a[1] < low[1]:
            low = a
        if left is None or a[0] < left[0]:
            left = a
        if right is None or a[0] > right[0]:
            right = a
    
    pts = [low, high, left, right]
    maxdist = 0
    for i in range(len(pts) - 1):
        for j in range(i+1, len(pts)):
            maxdist = max(maxdist, dist(pts[i], pts[j]))
    print(maxdist)

if __name__ == '__main__':
    main()
