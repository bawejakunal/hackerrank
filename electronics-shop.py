#!/bin/python3

# https://www.hackerrank.com/challenges/electronics-shop

import sys

def getMoneySpent(keyboards, drives, money):
    keybrd = sorted(keyboards, reverse=True)
    drvs = sorted(drives)
    spent = -1
    k = 0
    while k < len(keybrd):
        d = 0
        while d < len(drvs):
            price = keybrd[k] + drvs[d]
            if price > money:
                break
            else:
                spent = max(spent, price)
            d += 1
        k += 1
    return spent 
        

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
