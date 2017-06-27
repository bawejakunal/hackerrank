"""
https://www.hackerrank.com/challenges/the-power-sum
"""

def ways(k, x, n):
    remain = x - k**n
    if remain < 0:
        return 0
    elif remain == 0:
        return 1
    else:
        return ways(k+1, x, n) + ways(k+1, remain, n)

def main():
    x = int(input().strip())
    n = int(input().strip())
    print(ways(1, x, n))

if __name__ == '__main__':
    main()
