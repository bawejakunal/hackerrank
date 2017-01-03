"""
https://www.hackerrank.com/challenges/non-divisible-subset
"""

n, k = map(int, raw_input().strip().split())
s = map(int, raw_input().strip().split())

size = 0 #size of maximal set
count = [0 for _ in xrange(k)] #count of modulo k

for num in s:
    mod = num % k
    count[mod] += 1

#at most one element evenly divisible by k in maximal set
if count[0] > 0:
    size += 1

#modulo 1 to k/2, inclusive
for i in xrange(1, k/2 + 1):
    size += max(count[i], count[k-i])

"""
for even k, if count[k/2] > 1 then we can have at most 1
element in maximal set such that element % k = k/2
"""
if k % 2 == 0 and count[k/2] > 1:
    size -= count[k/2] - 1

print size
