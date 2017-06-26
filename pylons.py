"""
https://www.hackerrank.com/challenges/pylons
"""

def main():
    n, k = map(int, input().strip().split())
    twrs = list(map(int, input().strip().split()))
    cty = 0 # current city
    req = 0 # required towers
    while cty < n:
        # pick the farthest tower that can light the city
        _curr = None # farthest tower location
        for i in range(cty, min(cty + k, n)):
            if twrs[i] == 1:
                _curr = i # farther tower
        # no tower in k-1 distance on right so look left for nearest tower
        if _curr is None:
            for i in range(cty, max(cty-k, -1), -1):
                if twrs[i] == 1:
                    _curr = i
                    break
        # if still not found then break
        if _curr is None:
            break
        req += 1 # found a tower at k-1 distance
        cty = _curr + k # found tower can light next k-1 distance cities too
    
    # not all cities covered
    if cty < n:
        print(-1)
    else:
        print(req)

        
if __name__ == '__main__':
    main()