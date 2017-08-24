# https://www.hackerrank.com/challenges/jim-and-the-jokes

def main():
    N = int(input().strip())
    evts = dict()
    while N > 0:
        m, d = list(map(int, input().split()))
        try:
            e = int(str(d), m)
            evts[e] = evts.get(e, 0) + 1
        except ValueError:
            pass
        N -= 1
    cnt = 0
    for v in evts.values():
        cnt += v*(v-1)//2
    print(cnt)

if __name__ == '__main__':
    main()
