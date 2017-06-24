"""
https://www.hackerrank.com/challenges/beautiful-pairs
"""

from collections import Counter

def main():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    setB = Counter(B) # count of numbers in B
    count = 0
    for num in A:
        if num in setB and setB[num] > 0:
            count += 1
            setB[num] -= 1 # match numbers from A to B
    
    # all numbers matched
    if count == N:
        count -= 1 # exactly 1 number in B HAS to be changed
    
    # count < N i.e some number did not match
    else:
        count += 1
    print(count)
    
if __name__ == '__main__':
    main()