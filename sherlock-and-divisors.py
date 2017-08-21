"""
https://www.hackerrank.com/challenges/sherlock-and-divisors
"""

def getEvenDivisors(n):
    divs = set()
    for d in range(1, int(pow(n, 0.5)) + 1):
        if n % d == 0:
            if (d & 1) == 0:
                divs.add(d)
            q = n // d
            if (q & 1) == 0:
                divs.add(q)
    return divs

def main():
    t = int(input().strip())
    while t > 0:
        n = int(input().strip())
        cnt = 0
        if n & 1 == 0:      # check only if even number
            divs = getEvenDivisors(n)
            cnt = len(divs)
        print(cnt)
        t -= 1

if __name__ == '__main__':
    main()
