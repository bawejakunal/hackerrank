"""
https://www.hackerrank.com/challenges/recursive-digit-sum
"""

def digit_sum(x):
    if x == 0:
        return x
    return (x % 10) + digit_sum(x//10)

def super_digit(x):
    if x < 10:
        return x
    # otherwise
    return super_digit(digit_sum(x))

def main():
    n, k = input().strip().split()
    k = int(k)
    # n could be very large so represent as list of digits
    n = [int(x)*k for x in n] # each digit k times
    while len(n) > 1:
        n = list(map(super_digit, n))
        # combine step
        p = list()
        for i in range(0, len(n)-1, 2):
            p.append(n[i] + n[i+1])
        i += 2
        while i < len(n):
            p.append(n[i])
            i += 1
        n = p
    print(super_digit(n[0]))

if __name__ == '__main__':
    main()
