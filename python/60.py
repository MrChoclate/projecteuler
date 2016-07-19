"""
Prime pair sets
Problem 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""

import itertools
import math

def is_prime(x, prime_list, prime_set=None):
    if prime_set is not None and x < 10 ** 7:
        return x in prime_set

    for n in prime_list:
        if n > math.sqrt(x):
            return True
        if x % n == 0:
            return False
    raise 'limit reach'

def get_prime_list(limit):
    assert(limit >= 3)
    list_ = [2, 3]

    last = list_[-1]
    while last <= limit:
        last += 2
        if is_prime(last, list_):
            list_.append(last)

    return list_

def is_prime_set(s, prime_set, prime_list):
    for a, b in itertools.combinations(s, 2):
        c, d = int(str(a) + str(b)), int(str(b) + str(a))
        if not is_prime(c, prime_list, prime_set) or not is_prime(d, prime_list, prime_set):
            return False
    return True

def solve(prime_list, prime_set):
    sets = []
    for p in prime_list:
        add = False
        for s in list(sets):  # a copy because of sets.append below
            if is_prime_set(s.union([p]), prime_set, prime_list):
                sets.append(set(s))
                s.add(p)
                add = True
        if not add:
            sets.append(set([p]))
        for s in sets:
            if len(s) == 5:
                return sum(s)

if __name__ == '__main__':
    prime_list = get_prime_list(10 ** 6)
    prime_set = set(prime_list)
    assert(is_prime_set(set([3, 7, 109, 673]), prime_set, prime_list))
    print(solve(prime_list, prime_set))
