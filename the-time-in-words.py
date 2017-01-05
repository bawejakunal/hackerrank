#!/bin/python
"""
https://www.hackerrank.com/challenges/the-time-in-words
"""

h = int(raw_input().strip())
m = int(raw_input().strip())

dictionary = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'quarter',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'half'
}

string = None
if m == 0:
    string = dictionary[h] + " o' clock"
elif m == 1:
    string = dictionary[m] + " minute past " + dictionary[h]
elif m == 15 or m == 30:
    string = dictionary[m] + " past " + dictionary[h]
elif m < 21:
    string = dictionary[m] + " minutes past " + dictionary[h]
elif m < 30:
    string = dictionary[20] + " " + dictionary[m-20] + " minutes past " + dictionary[h]
else:
    h = h % 12 + 1
    m = 60 - m
    if m == 1:
        string = dictionary[m] + " minute to " + dictionary[h]
    elif m == 15:
        string = dictionary[m] + " to " + dictionary[h]
    elif m < 21:
        string = dictionary[m] + " minutes to " + dictionary[h]
    elif m < 30:
        string = dictionary[20] + " " + dictionary[m-20] + " minutes to " + dictionary[h]

print string
