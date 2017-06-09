# https://www.hackerrank.com/challenges/counting-valleys

N = int(input().strip())
S = input().strip()

h = 0
v = 0
for i in range(len(S)):
    if S[i] == 'U':
        h += 1
        if h == 0:
            v += 1
    else:
        h -= 1
print(v)
