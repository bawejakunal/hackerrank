#!/bin/python

"""
https://www.hackerrank.com/challenges/library-fine
"""

d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

fine = 0

#more than a year late
if y1 > y2:
    fine = 10000

#same calendar year
elif y1 == y2:
    #different calendar months
    if m1 > m2:
        fine = (m1 - m2) * 500

    #same month, late return
    elif m1 == m2 and d1 > d2:
        fine = (d1 - d2) * 15

    #returned on time
    else:
        fine = 0

#returned earlier than calendar year
else:
    fine = 0

print fine
