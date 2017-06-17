#!/bin/python3

# https://www.hackerrank.com/challenges/richie-rich

def richieRich(s, n, k):
    l = 0
    r = n-1
    arr = list(map(int, list(s)))
    mark = [0] * (n//2) # track the numbers that we change
    num = None
    while l < r:
        if arr[l] != arr[r]:
            k -= 1
            if k < 0:
                num = -1
                break
            if arr[l] < arr[r]:
                arr[l] = arr[r]
            else:
                arr[r] = arr[l]
            mark[l] = 1 # mark left num as changed
        l += 1
        r -= 1
    
    # not possible
    if num is not None and num < 0:
        return str(num)
    
    # start changing from outer side
    l = 0
    r = n - 1
    while l < r and k > 0:
        if arr[l] < 9:
            # touched before
            if mark[l] == 1:
                k -= 1
                arr[l] = 9
                arr[r] = 9
            elif k - 2 >= 0:
                k -= 2
                arr[l] = 9
                arr[r] = 9
        l += 1
        r -= 1
    # odd length and one digit is left
    if k > 0 and n % 2 == 1:
        arr[n//2] = 9
    num = "".join(map(str, arr))
    return num
        

n, k = map(int, input().strip().split())
s = input().strip()
result = richieRich(s, n, k)
print(result)
