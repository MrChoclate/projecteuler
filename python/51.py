"""
Prime digit replacements
Problem 51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime
 with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

import itertools

is_prime = __import__('3').is_prime
get_prime_list = __import__('3').get_prime_list

def make_family(x, prime_set, replace_tuple):
    x_ = str(x)
    nb = 0
    for digit in '0123456789'[1 if 0 in replace_tuple else 0:]:
        x_ = ''.join(digit if k in replace_tuple else c for k, c in enumerate(x_))
        if int(x_) in prime_set:
            nb += 1
    return nb

def brute_force(prime_list, prime_set):
    for p in prime_list:
        for c in set(str(p)):
            tuple_ = tuple(k for k, char in enumerate(str(p)) if char == c)
            if len(str(p)) in tuple_:
                break
            if make_family(p, prime_set, tuple_) == 8:
                return p

if __name__ == '__main__':
    prime_list = get_prime_list(10 ** 7)
    prime_set = set(prime_list)
    assert(make_family(56003, prime_set, (2,3)) == 7)
    print(brute_force(prime_list, prime_set))
