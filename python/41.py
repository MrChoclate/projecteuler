"""
Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

import math
import itertools


def is_prime(x):
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def gen_largest_pandigital_prime():
    for i in range(9):
        for x in itertools.permutations('987654321'[i:]):
            y = int(''.join(x))
            if is_prime(y):
                return y

if __name__ == '__main__':
    print(gen_largest_pandigital_prime())
