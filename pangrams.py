# https://www.hackerrank.com/challenges/pangrams
    
s = input().strip().lower()
c = [1] * 26
for ch in s:
    if 'a' <= ch <= 'z' and c[ord(ch)-97] > 0:
        c[ord(ch)-97] -= 1
if sum(c) > 0:
    print('not pangram')
else:
    print('pangram')
