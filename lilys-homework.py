"""
https://www.hackerrank.com/challenges/lilys-homework
"""

def count_swaps(arr, cpy):
    # compare pos and increment count
    pos = dict() # dictionary of integer positions
    for p, val in enumerate(cpy):
        pos[val] = p
    
    count = 0
    for i in range(len(cpy)):
        if arr[i] != cpy[i]:
            count += 1
            # perform the swap
            idx = pos[arr[i]] # index to put number to
            cpy[i], cpy[idx] = cpy[idx], cpy[i]
            # update pos for number swapped out of i
            pos[cpy[idx]] = idx
    return count

def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    cpy = list(arr) # copy of arr
    rev = list(reversed(arr)) # reversed copy of original array

    # sort original in O(nlogn)
    arr.sort()
    
    cnt1 = count_swaps(arr, cpy)
    cnt2 = count_swaps(arr, rev)
    print(min(cnt1, cnt2))

if __name__ == '__main__':
    main()