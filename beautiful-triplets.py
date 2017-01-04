"""
https://www.hackerrank.com/challenges/beautiful-triplets
"""

def main():
    """
    count beautiful triplets
    """
    n, d = map(int, raw_input().strip().split())
    arr = map(int, raw_input().strip().split())
    count = 0

    for i in xrange(n):
        triplet = 1 #one element of triplet
        """
        increasing sequence, so search till at most
        i+2d element
        """
        for j in xrange(i+1, min(n, 2*d + i + 1)):
            diff = arr[j] - arr[i]
            if diff == d or diff == 2*d:
                triplet += 1

        if triplet == 3:
            count += 1

    print count

if __name__ == '__main__':
    main()
