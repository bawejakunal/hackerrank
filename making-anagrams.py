#!/bin/python3

#https://www.hackerrank.com/challenges/making-anagrams

def makingAnagrams(s1, s2):
    count = [0] * 26
    dels = 0
    for ch in s1:
        count[ord(ch)-97] += 1
    for ch in s2:
        count[ord(ch)-97] -= 1
    for i in range(26):
        dels += abs(count[i])
    return dels

s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
