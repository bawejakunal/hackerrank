# https://www.hackerrank.com/challenges/possible-path/problem

from fractions import gcd

def main():
    T = int(input().strip())
    while T > 0:
        a, b, x, y = list(map(int, input().split()))
        c = gcd(a, b) == gcd(x, y)
        print('YES' if c else 'NO')
        T -= 1

if __name__ == '__main__':
    main()