# Sieve of Eratosthenes is an algorithm that finds all prime numbers up to a
# given n. The algorithm works by marking all multiples of each prime.

def sieveOfEratosthenes(n):
    primelist = [False] * 2 + [True] * (n - 1)
    for i in range(int(n ** 0.5 + 1.5)):
        if primelist[i]:
            for j in range(i * i, n, i):
                primelist[j] = False
    return [i for i, prime in enumerate(primelist) if prime]


print(sieveOfEratosthenes(999))
