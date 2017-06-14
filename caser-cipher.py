#!/bin/python3

# https://www.hackerrank.com/challenges/caesar-cipher-1

n = int(input().strip())
s = input().strip()
K = int(input().strip())

enc = ""
for ch in s:
    if 'a' <=ch <= 'z':
        enc += (chr((ord(ch) - 97 + K) % 26 + 97))
    elif 'A' <= ch <= 'Z':
        enc += (chr((ord(ch) - 65 + K) % 26 + 65))
    else:
        enc += ch
print(enc)