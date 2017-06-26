"""
https://www.hackerrank.com/challenges/jim-and-the-orders
"""

def main():
    n = int(input().strip())
    deliver = dict()
    for i in range(1, n+1):
        _dlvr = sum(map(int, input().strip().split()))
        if _dlvr not in deliver:
            deliver[_dlvr] = [i]
        else:
            tmp = deliver[_dlvr]
            tmp.append(i)
            deliver[_dlvr] = tmp
    ans = str()
    for time in sorted(deliver.keys()):
        for order in deliver[time]:
            ans += str(order) + " "
    
    print(ans)

if __name__ == '__main__':
    main()