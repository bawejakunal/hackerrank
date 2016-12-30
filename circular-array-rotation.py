"""
https://www.hackerrank.com/challenges/circular-array-rotation
"""

n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))

#identify final shift
k = k % len(a)

for a0 in xrange(q):
    m = int(raw_input().strip())
    m = (m - k) % n
    print a[m]
