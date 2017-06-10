# https://www.hackerrank.com/challenges/permutation-equation

n = int(input())
p = map(int, input().split())
pinv = [0] * (n+1)

for k, v in enumerate(p):
    pinv[v] = k+1

for x in range(1, n+1):
    print(pinv[pinv[x]])