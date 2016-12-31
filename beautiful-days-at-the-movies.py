"""
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def reverse(number):
    """
    assume positive number
    """
    reversed_number = 0
    while number > 0:
        reversed_number *= 10
        reversed_number += (number % 10)
        number /= 10
    return reversed_number

def main():
    """
    main work happens here
    """
    count = 0
    i, j, k = map(int, raw_input().strip().split())
    for date in xrange(i, j+1):
        if abs(date - reverse(date)) % k == 0:
            count += 1
    print count

if __name__ == '__main__':
    main()
