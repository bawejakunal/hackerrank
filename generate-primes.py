import math

def insert_primes(num, primes=list()):
    def is_prime(primes, num):
        if num < 2:
            return False
        sqrt = math.ceil(math.sqrt(num))
        for p in primes:
            if p > sqrt:
                break
            if num % p == 0:
                return False
        return True

    if len(primes) > 0 and primes[-1] >= num:
        return primes
    strt = primes[-1] + 1 if len(primes) > 0 else 1
    for i in range(strt, num + 1):
        if is_prime(primes, i):
            primes.append(i)
    return primes


# build a given list
primes = list()
insert_primes(10, primes)
print(primes)
insert_primes(11, primes)
print(primes)
insert_primes(12, primes)
print(primes)

# generate a new list
print(insert_primes(50))