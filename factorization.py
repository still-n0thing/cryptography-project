from typing import List, Set, Dict, Tuple, Optional
import random
from math import gcd, sqrt

def get_factors(n: int) -> List[int]:
    """
    Returns the list of all the factors
    """
    res = []
    i = 1
    while(i * i <= n):
        if n % i == 0:
            if n / i == i:
                res.append(i)
            else:
                res.append(i)
                res.append(n // i)
        i += 1
    return res

def binpow(base, exponent, mod):
    res = 1
    while exponent > 0:
        if (exponent & 1):
            res = (res * base) % mod
        exponent >>= 1
        base = (base * base) % mod
    return res

def PollardRho(n):
    if n == 1:
        return n
    if n % 2 == 0:
        return 2
    
    x = random.randint(0, 2) % (n - 2)
    y = x
    c = random.randint(0, 1) % (n - 1)
    d = 1

    while d == 1:
        x = (binpow(x, 2, n) + c + n) % n
        y = (binpow(y, 2, n) + c + n) % n
        y = (binpow(y, 2, n) + c + n) % n

        d = gcd(abs(x - y), n)

        if d == n:
            return PollardRho(n)
    
    return d

def dixon_factorization(n):
    base = [2, 3, 5, 7]

    start = int(sqrt(n))
    pairs = []

    for i in range(start, n):
        for j in range(len(base)):
            lhs = binpow(i, 2, n)
            rhs = binpow(i, 2, n)
            if lhs == rhs:
                pairs.append([i, base[j]])
    
    new = []
    
    for i in range(len(pairs)):
        factor = gcd(pairs[i][0] - pairs[i][1], n)
        if factor != 1:
            new.append(factor)
    
    return list(set(new))

if __name__ == '__main__':
    from RSA import random_RSA, RSA
    rsa = random_RSA()
    print(rsa)
    n = rsa[0][1]
    res = []
    print(get_factors(n))
    for num in get_factors(n):
        if num != 1 and num != n:
            res.append(num)
    print(res)
    print(RSA(*res))