# O(NloglogN)
def eratosthenes_sieve(n):
    is_prime = [True]*(n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
        if is_prime[p]:
            for q in range(2*p, n + 1, p):
                is_prime[q] = False
    return is_prime
n = 10
is_prime = eratosthenes_sieve(n)
print(is_prime[5]) # True
print(is_prime[10]) # False
print(is_prime)