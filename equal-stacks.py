#!/bin/python3
"""
https://www.hackerrank.com/challenges/equal-stacks/

Do not overthink !
"""

n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
s1 = [int(h1_temp) for h1_temp in input().strip().split(' ')][::-1]
s2 = [int(h2_temp) for h2_temp in input().strip().split(' ')][::-1]
s3 = [int(h3_temp) for h3_temp in input().strip().split(' ')][::-1]
h1 = sum(s1)
h2 = sum(s2)
h3 = sum(s3)

while not (h1 == h2 == h3):
    h = min(h1, h2, h3) # shortest stack
    if h2 == h:
        s1, h1, s2, h2 = s2, h2, s1, h1
    elif h3 == h:
        s1, h1, s3, h3 = s3, h3, s1, h1
    while h2 > h1:
        h2 -= s2.pop()
    while h3 > h1:
        h3 -= s3.pop()

print(h1)
