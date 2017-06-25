"""
https://www.hackerrank.com/challenges/largest-permutation
"""

def main():
    N, K = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    position = dict()
    for i in range(N):
        position[arr[i]] = i
    
    i = 0
    while K > 0 and i < N:
        if arr[i] != (N - i):
            K -= 1 # now we swap
            idx = position[N-i]
            arr[i], arr[idx] = N-i, arr[i] #update values
            position[arr[idx]], position[N-i] = idx, i # update positions
        i += 1
    
    print(" ".join(map(str, arr)))

if __name__ == '__main__':
    main()