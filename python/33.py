"""
Digit cancelling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

import itertools
import fractions

digits = '0123456789'

def gen_frac():
    for a, b in itertools.product(itertools.permutations(digits, 2), repeat=2):
        a, b = ''.join(a), ''.join(b)
        if int(a) < int(b) and set(a) & set(b):
            digit = list(set(a) & set(b))[0]
            frac = int(a) / int(b)
            if digit != '0' and int(b.replace(digit, '')):
                simpl = int(a.replace(digit, '')) / int(b.replace(digit, ''))
                if frac == simpl:
                    yield a, b

if __name__ == '__main__':
    num, dem = 1, 1
    for a, b in gen_frac():
        num, dem = num * int(a), dem * int(b)
    print(dem / fractions.gcd(num, dem))
