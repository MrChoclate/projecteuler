"""
Pandigital products
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

# a * b = c
# log(a) + log(b) = log(c) < 9
# c <= 10 ** 4.5
# a <= 10 ** 4.5 / b. b > 1
# a <= 10 ** 4.5 / 2

import itertools

def is_product_pandigital(a, b):
    c = a * b
    a, b, c = str(a), str(b), str(c)
    if any(len(x) != len(set(x)) for x in (a, b, c)):
        return False

    a, b, c = set(a), set(b), set(c)
    return (a | b | c) == set('123456789') and \
           len(a & b) == 0 and len(a & c) == 0 and len(b & c) == 0

if __name__ == '__main__':
    assert(is_product_pandigital(39, 186))
    list_ = [a * b for a in range(1, int(10 ** 4.5 / 2))
                   for b in range(a + 1, int(10 ** 4.5 / a))
                   if is_product_pandigital(a, b)]

    print(sum(set(list_)))
