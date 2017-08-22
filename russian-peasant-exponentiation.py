# https://www.hackerrank.com/challenges/russian-peasant-exponentiation/

def getPow(a, k, m=1):
    p = a.copy()
    while ((k & 1) == 0):
        p = [(p[0]*p[0] - p[1]*p[1]) % m, (2*p[0]*p[1]) % m]
        k >>= 1
    pr = p.copy()
    k >>= 1
    while k > 0:
        p = [(p[0]*p[0] - p[1]*p[1]) % m, (2*p[0]*p[1]) % m]
        if (k & 1) == 1:
            pr = [(pr[0]*p[0] - pr[1]*p[1]) % m, (pr[0]*p[1] + p[0]*pr[1]) % m]
        k >>= 1
    return pr

def main():
    q = int(input().strip())
    while q > 0:
        a, b, k, m = list(map(int, input().split()))
        c, d = getPow([a,b], k, m)
        print(c, d)
        q -= 1

if __name__ == '__main__':
    main()
    