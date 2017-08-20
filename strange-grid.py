# https://www.hackerrank.com/challenges/strange-grid

import math

r, c = list(map(int, input().split()))
s = int(math.ceil(r/2)) - 1             #0th 1st 2nd set of rows and so on
n = s * 10                              # n is the number we construct
n += 1 - (r & 1)                        # odd rows have even and vice versa
n += (c - 1) << 1
print(n)
