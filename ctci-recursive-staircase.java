# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    w = [1] * min(3, n+1)
    for i in range(1, min(3, n+1)):
        w[i] = i    # less than 3
    for i in range(3, n+1):
        n = sum(w)
        w = w[1:] + [n]
    print(w[-1])
        