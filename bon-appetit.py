"""
https://www.hackerrank.com/challenges/bon-appetit
"""

def main():
    """
    The hackerrank link expects answer to be always integer, but that
    should not be the case, even fractional costs should be allowed
    and hence fractional cost differences, so ideally no need to
    typecast on line 24
    """
    n, k = map(int, raw_input().strip().split())
    cost = map(int, raw_input().strip().split())
    charged = float(raw_input().strip())

    correct = 0
    for i in xrange(n):
        if i != k:
            correct += cost[i] / 2.0 #split the item cost except kth item

    if correct == charged:
        print 'Bon Appetit'
    else:
        print int(charged - correct)

if __name__ == '__main__':
    main()
