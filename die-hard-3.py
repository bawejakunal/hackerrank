# https://www.hackerrank.com/challenges/die-hard-3/problem

from fractions import gcd

def main():
    t = int(input().strip())
    while t > 0:
        a,b,c = list(map(int,input().split()))
        x = gcd(a, b)
        if (c % x) == 0 and (c <= a or c <= b):
            print('YES')
        else:
            print('NO')
        t -= 1

if __name__ == '__main__':
    main()
