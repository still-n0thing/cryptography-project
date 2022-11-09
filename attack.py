from typing import List, Set, Dict, Tuple, Optional, Iterator
import random
from math import gcd
from RSA import gcd_extended

def attack_without_e(p: int, q: int, e: int) -> Iterator[Tuple[Tuple[int, int], Tuple[int, int]]]:
    n = p * q

    #totient : phi(n)
    phi = (p - 1) * (q - 1)

    for e in range(1, phi - 1):
        if gcd(e, phi) == 1:
            d = gcd_extended(e, phi)
            yield ((e, n), (d, n))

def attack(p: int, q: int, e: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    n = p * q

    #totient : phi(n)
    phi = (p - 1) * (q - 1)

    d = gcd_extended(e, phi)
    return ((e, n), (d, n))    

if __name__ == "__main__":
    from RSA import random_RSA, RSA
    from factorization import get_factors
    rsa = random_RSA()
    print(rsa)
    e, n = rsa[0]
    res = []
    print(get_factors(n))
    for num in get_factors(n):
        if num != 1 and num != n:
            res.append(num)
    p, q = res
    print(attack(p, q, e))