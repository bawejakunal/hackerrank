"""
https://www.hackerrank.com/challenges/kaprekar-numbers
"""

import sys

def is_kaprekar(number):
    """
    check modified kaprekar number
    """
    square = str(number ** 2)
    try:
        first = int(square[:len(square)/2])
    except ValueError:
        first = 0

    try:
        second = int(square[len(square)/2:])
    except ValueError:
        second = 0

    return first + second == number


def main():
    """
    Modified kaprekar numbers
    """
    p = int(raw_input().strip())
    q = int(raw_input().strip())
    count = 0
    for number in xrange(p, q+1):
        if is_kaprekar(number):
            sys.stdout.write("%d " % number)
            count += 1

    if count == 0:
        print 'INVALID RANGE'

if __name__ == '__main__':
    main()
