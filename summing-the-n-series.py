# https://www.hackerrank.com/challenges/summing-the-n-series

MODULO = 1000000007

def main():
    t = int(input())
    while t > 0:
        n = int(input()) % MODULO
        ans = pow(n, 2, MODULO)
        print(ans)
        t -= 1

if __name__ == '__main__':
    main()
