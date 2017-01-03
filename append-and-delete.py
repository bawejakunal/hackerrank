#!/bin/python

"""
https://www.hackerrank.com/challenges/append-and-delete
"""

s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

size = 0
total_len = len(s) + len(t)

"""
Case 1: len(s) + len(t) <= k: truncate s completely and make t again
        as deletion from empty string results in empty string again
        we can have cases like "ab", "cd", 7, so perform 5 deletions
        and 2 appends
"""
if total_len <= k:
    print 'Yes'

else:
    for pair in zip(s, t):
        if pair[0] != pair[1]:
            break
        size += 1

    operations = total_len - (2 * size)
    """
    Case 2: @operations: expected operations
            operations should be at most k, additionally if k is even then
            required operations should also be even, or odd if k is odd.
            eg: "abcdefghijk", "abcdef", 6 => No
            "abcdefghijk", "abcdef", 7 => Yes, delete f and add again
    """
    if (operations <= k) and (operations % 2 == k % 2):
        print 'Yes'
    else:
        print 'No'
