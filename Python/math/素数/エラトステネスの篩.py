def sieve_eratosthenes(n):
    primes = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = 0
    primes[2] = 1
    for p in range(3, n + 1, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p):
                primes[q] = 0
    return primes

n = 11
primes = sieve_eratosthenes(n)
print(primes[5])
print(primes[10])
print(primes)