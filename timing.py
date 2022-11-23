import time

from RSA import random_RSA, RSA
from factorization import get_factors, PollardRho, dixon_factorization
from attack import attack

P, Q = 13, 17

rsa = RSA(P, Q)
print("RSA")
print(rsa)

e, n = rsa[0] # public information

checkpoints = []
methods = []

def trace(name = ""):
    global checkpoints, methods
    checkpoints.append(time.time())
    methods.append(name)

trace()

print()
print("Basic Factorization")
res = []
for num in get_factors(n):
    if num != 1 and num != n:
        res.append(num)
p, q = res
print(attack(p, q, e))
trace("Basic Factorization")

print()
print("Pollard Rho Prime Factorization")
p = PollardRho(n)
q = n // p
print(attack(p, q, e))
trace("Pollard Rho Prime Factorization")

print()
print("Dixon Factorization")
res = []
for num in dixon_factorization(n):
    if num != 1 and num != n:
        res.append(num)
p, q = res
print(attack(p, q, e))
trace("Dixon Factorization")

print()
for i in range(1, len(checkpoints)):
    diff = checkpoints[i] - checkpoints[i - 1] 
    print(f"{methods[i]}: {diff * (10 ** 6)} µsec")
