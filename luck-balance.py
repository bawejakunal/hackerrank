# https://www.hackerrank.com/challenges/luck-balance

def main():
    N, K = map(int, input().strip().split())
    maximal = list()
    luck = 0
    while N > 0:
        L, T = map(int, input().strip().split())
        if T == 1:
            if K == 0:
                luck -= L # win
            elif len(maximal) < K:
                maximal.append(L)
            else:
                idx = maximal.index(min(maximal)) # smallest luck to replace
                if L > maximal[idx]:
                    luck -= maximal[idx] # win
                    maximal[idx] = L
                else:
                    luck -= L
        else:
            luck += L # lose non important games
        N -= 1
    luck += sum(maximal) # losing games
    print(luck)


if __name__ == '__main__':
    main()