#!/bin/python3

# https://www.hackerrank.com/challenges/funny-string

def funnyString(s):
    r = s[::-1]
    result = "Funny"
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i])-ord(r[i-1])):
            result = "Not Funny"
            break
    return result

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
