#!/bin/python
"""
https://www.hackerrank.com/challenges/happy-ladybugs
"""

g = int(raw_input().strip())
for _ in xrange(g):
    n = int(raw_input().strip())
    b = raw_input().strip()
    color = [0 for i in xrange(26)] #count colors
    happy = True
    #check already happy configuration
    for i in xrange(n):
        if 'A' <= b[i] <= 'Z':
            color[ord(b[i]) - ord('A')] += 1
            if i == 0 and i == n-1:
                happy = False #lone ladybug cant be happy
            elif i == n - 1 and b[i] != b[i - 1]:
                happy = False #last lady bug is not happy
            elif b[i] != b[i - 1] and b[i] != b[i+1]:
                happy = False #middle ladybug not happy

    if happy is True:
        print 'YES' #already happy configuration
    else:
        #no moves possible then no solution
        #lone ladybug of a color cant be made happy
        if '_' not in b or 1 in color:
            print 'NO'
        else:
            print 'YES'
