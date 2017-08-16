# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

def array_left_rotation(a, n, k):
    k = k % n
    b = a.copy()
    if k > 0:
        b = b[k:] + b[:k]
    return b
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
