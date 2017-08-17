# https://www.hackerrank.com/challenges/ctci-making-anagrams

from collections import Counter

def number_needed(a, b):
    counts = Counter(a)
    for c in b:
        counts[c] = counts.get(c, 0) - 1
    return sum(map(abs, counts.values()))

a = input().strip()
b = input().strip()

print(number_needed(a, b))
