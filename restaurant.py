# https://www.hackerrank.com/challenges/restaurant

def main():
    t = int(input().strip())
    while t > 0:
        l, b = list(map(int, input().split()))
        l, b = max(l, b), min(l, b)
        num = 0
        for parts in range(1, 1 + b):
            side = b // parts
            if (b % side == 0) and (l % side == 0):
                num = (l//side) * (b//side)
                break
        print(num)
        t -= 1

if __name__ == '__main__':
    main()
