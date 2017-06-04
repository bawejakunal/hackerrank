"""
https://www.hackerrank.com/challenges/reduced-string

Sometimes simplest answer is the best answer !
"""

s = input().strip()
has_dup = True
while has_dup:
    has_dup = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            has_dup = True
            break # out of for loop

if s == "":
    s = "Empty String"
print(s)