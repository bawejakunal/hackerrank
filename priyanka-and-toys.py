"""
https://www.hackerrank.com/challenges/priyanka-and-toys
"""

def main():
    N = int(input().strip())
    W = sorted(map(int, input().strip().split()))
    i = 0
    units = 0
    while i < N:
        _lower = W[i]
        _upper = W[i] + 4
        units += 1 # starting a new unit
        while i < N and W[i] <= _upper:
            i += 1
    print(units)


if __name__ == '__main__':
    main()
