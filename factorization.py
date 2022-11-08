from typing import List, Set, Dict, Tuple, Optional
import random

def get_fectors(n: int) -> List[int]:
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
    return res

if __name__ == '__main__':
    from RSA import random_RSA
    rsa = random_RSA()
    print(rsa)