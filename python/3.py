"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import math

def is_prime(x, prime_list):
    for n in prime_list:
        if n > math.sqrt(x):
            return True
        if x % n == 0:
            return False

def get_prime_list(limit):
    assert(limit >= 3)
    list_ = [2, 3]

    last = list_[-1]
    while last <= limit:
        last += 2
        if is_prime(last, list_):
            list_.append(last)

    return list_

def prime_factors(x):
    prime_list = get_prime_list(math.sqrt(x))
    factors = [p for p in prime_list if x % p == 0]
    return factors

if __name__ == '__main__':
    assert(prime_factors(13195) == [5, 7, 13, 29])
    print(max(prime_factors(600851475143)))
