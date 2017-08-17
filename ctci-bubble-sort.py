# https://www.hackerrank.com/challenges/ctci-bubble-sort

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
total_swaps = 0
for i in range(n):
    swaps = 0
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swaps += 1
    if swaps == 0:
        break
    total_swaps += swaps

print("Array is sorted in %d swaps." % total_swaps)
print("First Element:", a[0])
print("Last Element:", a[-1])