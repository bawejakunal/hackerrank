# https://www.hackerrank.com/challenges/ctci-big-o

def is_prime(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    for p in range(2, 1 + int(pow(n, 0.5))):
        if n % p == 0:
            return False
    return True

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    print('Prime' if is_prime(n) else 'Not prime')