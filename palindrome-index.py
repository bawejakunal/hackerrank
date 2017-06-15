#!/bin/python3

# https://www.hackerrank.com/challenges/palindrome-index

def palindromeIndex(s):
    # Complete this function
    if s == s[::-1]:
        return -1
    else:
        # check till middle character
        for i in range(0, (len(s)//2)+1):
            # at point of difference try to delete both characters
            if s[i] != s[len(s)-1-i]:
                # either first char should be deleted
                t = s[:i] + s[i+1:]
                if t == t[::-1]:
                    return i
                # or second char should be deleted
                t = s[:len(s)-1-i] + s[len(s)-i:]
                if t == t[::-1]:
                    return len(s)-1-i
                # otherwise impossible
                return -1

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)
