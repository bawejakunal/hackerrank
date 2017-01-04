#!/bin/python
"""
https://www.hackerrank.com/challenges/taum-and-bday
"""

import sys

t = int(raw_input().strip())
for _ in xrange(t):
    b, w = raw_input().strip().split(' ')
    b, w = [long(b), long(w)]
    x, y, z = raw_input().strip().split(' ')
    x, y, z = [long(x), long(y), long(z)]

    price = 0
    #convert black to white
    if x + z < y:
        price = (b + w) * x + w * z

    #convert white to black
    elif y + z < x:
        price = (b + w) * y + b * z

    else:
        price = b * x + w * y

    print price
