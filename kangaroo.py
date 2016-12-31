#!/bin/python

"""
https://www.hackerrank.com/challenges/kangaroo
x1 + v1.n = x2 + v2.n
n = float(x2 - x1)/(v1 - v2)
if n > 0 and whole integer then possible because the 
kangaroo starting at lesser position will be able to
catch up AND land at exactly same position as the
kangaroo with a head start
"""

import sys

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2 ,v2 = [int(x1),int(v1),int(x2),int(v2)]

#avoid division by zero
if v1 == v2:
    print 'NO'

else:
    n = float(x2 - x1)/(v1 - v2)
    # given x1 < x2, so n can not be 0
    if n > 0 and n.is_integer():
        print 'YES'
    else:
        print 'NO'
