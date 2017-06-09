#!/bin/python3

# https://www.hackerrank.com/challenges/day-of-the-programmer

def is_leap(year):
    # julian
    leap = year < 1918 and year % 4 == 0
    #gregorian
    leap = leap or (year % 100 == 0 and year % 400 == 0)
    leap = leap or (year % 100 != 0 and year % 4 == 0)
    return leap
            
def solve(year):
    eg_mths = None
    if year < 1918 or year > 1918:
        if is_leap(year):
            eg_mths = 244
        else:
            eg_mths = 243
    else:
        eg_mths = 230
    
    date = 256 - eg_mths
    return "%02d.%02d.%04d" % (date, 9, year)

year = int(input().strip())
result = solve(year)
print(result)
