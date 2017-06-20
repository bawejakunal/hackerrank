"""
https://www.hackerrank.com/challenges/fraudulent-activity-notifications
"""
from collections import Counter

n, d = map(int, input().split())
arr = list(map(int, input().split()))

def find(dic, idx):
    cnt = 0
    for i in range(201):
        cnt += dic.get(i, 0)
        if cnt >= idx:
            return i
        
ans = 0
dic = Counter(arr[:d])
for i in range(d, n):
    val = arr[i]
    med = find(dic, d//2 + d%2)
    if d % 2 == 0:
        ret = find(dic, (d//2)+1)
        med += ret
    else:
        med *= 2

    if val >= med:
        ans += 1

    # for next iteration
    dic[val] = dic.get(val, 0) + 1
    prev = arr[i - d]
    dic[prev] -= 1

print(ans)