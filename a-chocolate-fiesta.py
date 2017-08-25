# https://www.hackerrank.com/challenges/a-chocolate-fiesta

MOD = 10**9 + 7

def main():
    N = int(input().strip())
    a = list(map(int, input().split()))
    e = 0
    for n in a:
        if 0 == (n & 1):
            e += 1
    even = (1 << e) - 1
    odd = 0
    if e < N:
        odd = (1 << (N - e - 1)) - 1
    t = (odd % MOD + even % MOD) % MOD    
    t = (t + (odd * even) % MOD) % MOD
    print(t)

if __name__ == '__main__':
    main()
