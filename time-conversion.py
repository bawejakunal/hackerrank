#!/bin/python
"""
https://www.hackerrank.com/challenges/time-conversion?h_r=next-challenge&h_v=zen
"""

time = raw_input().strip()
hour = int(time[:2])

if time[-2:] == 'PM' and hour != 12:
    hour += 12
elif time[-2:] == 'AM' and hour == 12:
    hour = 0

print ("%02d" % hour) + time[2:-2]
    