from typing import List, Set, Dict, Tuple, Optional
import random

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

# TODO: 
# - Implement Pollards Rho Algorithm https://www.geeksforgeeks.org/pollards-rho-algorithm-prime-factorization/

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