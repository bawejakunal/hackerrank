# https://www.hackerrank.com/challenges/sherlock-and-moving-tiles

def main():
    L, s1, s2 = list(map(int, input().split()))
    D = pow(2*pow(L, 2), 0.5)
    s = abs(s1 - s2)   # relative speed
    q = int(input())
    while q > 0:
        a = int(input())    # query area
        d = pow(a*2, 0.5)    # diagonal of inner square
        t = (D - d)/s
        print(t)
        q -= 1

if __name__ == '__main__':
    main()