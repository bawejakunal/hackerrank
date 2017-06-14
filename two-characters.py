#!/bin/python3

# https://www.hackerrank.com/challenges/two-characters

def is_alternating(string):
    answer = len(string) > 1 and string[0] != string[1]
    if answer:
        sub = string[:2]
        for i in range(0,len(string)-1,2):
            if string[i:i+2] != sub:
                answer = False
                break
        if answer and len(string) % 2 == 1:
            answer = string[-1] == string[0]
    return answer

s_len = int(input().strip())
s = input().strip()
chars = list(set(s))
lngth = 0
if len(chars) > 1:
    for i in range(len(chars) - 1):
        c1 = chars[i]
        for c2 in chars[i+1:]:
            temp = s
            for ch in chars:
                if ch != c1 and ch != c2:
                    temp = temp.replace(ch, "")
            if is_alternating(temp):
                lngth = max(lngth, len(temp))

print(lngth)
    
    
