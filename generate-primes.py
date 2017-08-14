import math

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

def insert_primes(primes, num):
  if len(primes) > 0 and primes[-1] >= num:
    return
  strt = primes[-1] + 1 if len(primes) > 0 else 1
  for i in range(strt, num + 1):
    if is_prime(primes, i):
      primes.append(i)
  return

primes = list()
insert_primes(primes, 10)
print(primes)
insert_primes(primes, 11)
print(primes)
insert_primes(primes, 12)
print(primes)