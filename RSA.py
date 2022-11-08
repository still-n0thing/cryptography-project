from typing import List, Set, Dict, Tuple, Optional
import random

def sieve(n: int) -> List[int]:
    """
    Returns a list prime numbers till n
    """
    N = (n + 1)
    isprime = [True] * N
    prime = []
    SPF = [None] * N

    isprime[0] = isprime[1] = False

    for i in range(2, N):
        if isprime[i] == True:
            prime.append(i)
            SPF[i] = i
        j = 0
        while (j < len(prime) and i * prime[j] < N and prime[j] <= SPF[i]):
            isprime[i * prime[j]] = False
            SPF[i * prime[j]] = prime[j]
            j += 1
    return prime


def gcd(a: int, b: int) -> int:
    """
    Returns gcd of a and b
    """
    return a if b == 0 else gcd(b, a % b)


def gcd_extended(a: int, b: int) -> int:
    """
    Returns modular multiplicative inverse of a under modulo b
    """
    m0 = b
    y = 0
    x = 1

    if (b == 1):
        return 0

    while (a > 1):
        q = a // b
        t = b

        b = a % b
        a = t
        t = y

        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x


def RSA(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Returns (e, n) public key and (d, n) private key as ((e, n), (d, n))
    """
    n = p * q

    #totient : phi(n)
    phi = (p - 1) * (q - 1)

    # finding e
    e = random.randint(2, phi - 1)
    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e += 1

    # finding d
    d = gcd_extended(e, phi)

    return ((e, n), (d, n))

def random_RSA(limit = 10 ** 5) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    mxn = limit
    primes = sieve(mxn)
    p, q = random.choices(primes, k=2)
    return RSA(p, q)

if __name__ == '__main__':
    mxn = 10 ** 7
    primes = sieve(mxn)
    p, q = random.choices(primes, k=2)
    print(f'p = {p}')
    print(f'q = {q}')
    print(f'((e, n), (d, n)) = {RSA(p, q)}')
