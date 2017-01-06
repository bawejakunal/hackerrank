#!/bin/python
"""
https://www.hackerrank.com/challenges/flatland-space-stations
"""

from math import floor

n, m = map(int, raw_input().strip().split(' '))
station = map(int,raw_input().strip().split(' '))
station.sort()

farthest = 0

"""
Edge case: city at end 0 without space station
"""
farthest = max(farthest, station[0])

"""
Maximum distance for astronauts in cities between the end
stations, this does not considers the edge case of astronauts
on end cities with no station
"""
for i in xrange(m - 1):
    distance = station[i + 1] - station[i]
    #ignore adjacent space stations
    if distance > 1:
        distance /= 2.0
        distance = int(floor(distance))
        farthest = max(farthest, distance)

"""
Edge case: city at end n-1 without space station
"""
farthest = max(farthest, n - 1 - station[m - 1])

print farthest
