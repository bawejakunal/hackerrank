#!/bin/python

"""
https://www.hackerrank.com/challenges/mini-max-sum
"""

a,b,c,d,e = raw_input().strip().split(' ')
l = [int(a),int(b),int(c),int(d),int(e)]

maximum = l[0]
minimum = l[0]

for i in xrange(1,len(l)):
    maximum = l[i] if l[i] > maximum else maximum
    minimum = l[i] if l[i] < minimum else minimum

"""
maximum = max(l)
minimum = min(l)
"""

total = sum(l)
print total - maximum, total - minimum
