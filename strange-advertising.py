"""
https://www.hackerrank.com/challenges/strange-advertising
"""

from math import floor

def main():
    """
    Track the number of people who liked the advertisement
    """
    days = int(raw_input().strip())
    count = 0
    current = 0

    # intialize day 1
    # this helps to avoid checking if day == 1
    # on each iteration of for loop
    if days > 0:
        current = floor(5 / 2.0)
        count += current

    # count for rest of days
    for day in xrange(2, days + 1):
        current = floor(current * (3 / 2.0))
        count += current

    print int(count)

if __name__ == '__main__':
    main()
