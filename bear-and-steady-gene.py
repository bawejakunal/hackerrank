"""
https://www.hackerrank.com/challenges/bear-and-steady-gene

Hint at bottom
"""

from collections import Counter

def main():
    """
    main method
    """
    n = int(input().strip())
    g = input().strip()
    t = n // 4 # target ideal count
    gd = Counter(g) # count proteins
    ptrn = ""
    ptrnd = dict()
    for _p in gd:
        c = gd.get(_p, 0) - t # update difference with target count
        if  c > 0:
            ptrn += _p * c
            ptrnd[_p] = c
    # now task is to find shortest substring in g which contains all chars from ptrn
    minlen = n
    gd = dict() # fresh dict to count chars in gene
    cnt = 0
    strt = 0
    # no pattern to be searched
    if len(ptrn) == 0:
        minlen = 0
    else:
        for i in range(n):
            gd[g[i]] = gd.get(g[i], 0) + 1
        
            if g[i] in ptrnd and gd[g[i]] <= ptrnd[g[i]]:
                cnt += 1
        
            if cnt == len(ptrn):
                # shrink the length
                # either g[strt] not in pattern or g[strt] is in ptrn but counted
                # more than required times in gd
                while g[strt] not in ptrnd or ptrnd[g[strt]] < gd[g[strt]]:
                    if g[strt] in ptrnd and ptrnd[g[strt]] < gd[g[strt]]:
                        gd[g[strt]] -= 1
                    strt += 1
                
                # update min length
                length = i - strt + 1
                if length < minlen:
                    minlen = length
                    # update latest strt here if required to track the smallest substr
    
    print(minlen)

if __name__ == '__main__':
    main()


# http://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/