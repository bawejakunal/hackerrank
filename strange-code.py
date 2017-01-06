#!/bin/python
"""
https://www.hackerrank.com/challenges/strange-code
Hint: geometric progression
"""

t = int(raw_input().strip())
cycles = 0 #cycles completed
compare = t/3.0 + 1
while 2 ** cycles < compare:
    cycles += 1
cycles -= 1 #number of full cycles completed before current cycle

start_time = 3 * ((2 ** cycles) - 1) + 1
start_count = 3 * (2 ** cycles)

t_count = start_count - (t - start_time)
print t_count
