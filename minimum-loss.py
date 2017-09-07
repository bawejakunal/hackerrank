"""
https://www.hackerrank.com/challenges/minimum-loss
"""

def minLoss(price, n):
    minloss = 999999999999999
    cpy = price.copy()
    cpy.sort()
    for i in range(1, len(cpy)):
        if (cpy[i]-cpy[i-1]) < minloss:
            if price.index(cpy[i]) < price.index(cpy[i-1]):
                minloss = cpy[i]-cpy[i-1]
    return minloss

def main():
    n = int(input().strip())
    p = list(map(int, input().split()))
    print(minLoss(p, n))

if __name__ == '__main__':
    main()
