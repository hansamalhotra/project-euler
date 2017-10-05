#prime factorisation

import random

# using fermat's primality test to generate prime numbers

def prime_numbers(a,b) :
    for i in range(a,b):
        m = random.randrange(1, i)
        n = random.randrange(1, i)
        if (m**(i-1)) % i == 1 and (n**(i-1)) % i == 1:
            yield i


q = 600851475143
for p in prime_numbers(2, 10000):
    while q % p == 0:
        q = q/p
    if q == 1:
        prime = p
        break
print("Greatest prime factor is ", prime)

