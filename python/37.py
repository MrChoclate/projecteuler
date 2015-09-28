"""
Truncatable primes
Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import math

def is_prime(x, prime_list):
    for n in prime_list:
        if n > math.sqrt(x):
            return True
        if x % n == 0:
            return False

def is_truncable(p, prime_list):
    x = p = str(p)
    while p:
        if int(p) not in prime_list:
            return False
        p = p[1:]
    while x:
        if int(x) not in prime_list:
            return False
        x = x[:-1]
    return True


def get_truncable_primes():
    truncatable = []
    list_ = [2, 3, 5, 7]
    set_ = set(list_)

    last = list_[-1]
    while len(truncatable) < 11:
        last += 2
        if is_prime(last, list_):
            list_.append(last)
            set_.add(last)
            if is_truncable(last, set_):
                truncatable.append(last)

    return truncatable

if __name__ == '__main__':
    print(sum(get_truncable_primes()))
