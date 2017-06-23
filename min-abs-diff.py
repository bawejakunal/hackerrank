#!/bin/python3

# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# your code goes here
a.sort()
diff = abs(a[-1]-a[0]) # max possible
for i in range(n-1):
    diff = min(diff, abs(a[i]-a[i+1]))
print(diff)
