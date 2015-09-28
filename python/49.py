"""
Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

import itertools

get_prime_list = __import__('3').get_prime_list

def solve(prime_list):
    s = set(prime_list)
    for p in prime_list:
        pset = s & set(int(''.join(x)) for x in itertools.permutations(str(p)))
        if len(pset) > 3:
            for p in itertools.combinations(pset, 3):
                a, b, c = sorted(list(p))
                if b - a == c - b and a != 1487 and \
                   len(str(a)) == len(str(b)) == len(str(c)) == 4:
                    return ''.join(str(x) for x in (a, b, c))

if __name__ == '__main__':
    l = get_prime_list(10 ** 4)
    print(solve(l))
