"""
Highly divisible triangular number
Problem 12

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""

import math
import sys
import functools

# n * (n + 1) < 2 * c
# n > - 1 + sqrt(1 + 4 * 2 * c) / 2

def is_prime(x, prime_list):
    for n in prime_list:
        if n > math.sqrt(x):
            return True
        if x % n == 0:
            return False

def decompose(x):
    d = {}
    for p in prime_list:
        if x == 1:
            break
        while x % p == 0:
            d[p] = d.get(p, 0) + 1
            x = x // p
    return d

@functools.lru_cache(maxsize=None)
def nb_divisors(x):
    res = 1
    for v in decompose(x).values():
        res *= v + 1
    return res

def nb_divisors_triangle(x):
    if x % 2 == 0:
        return nb_divisors(x / 2) * nb_divisors(x + 1)
    else:
        return nb_divisors(x) * nb_divisors((x + 1) / 2)

def gen_consecutive(nb):
    i = 1
    while nb_divisors_triangle(i) < nb:
        i += 1
    return i * (i + 1) / 2

if __name__ == '__main__':
    prime_list = [2, 3, 5, 7]
    last = prime_list[-1]
    while len(prime_list) < 100:
        last += 2
        if is_prime(last, prime_list):
            prime_list.append(last)

    print(int(gen_consecutive(int(sys.argv[1]))))
