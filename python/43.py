"""
Sub-string divisibility
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import itertools

def gen_pandigital():
    for x in itertools.permutations('0123456789'):
        if x[0] != '0':
            yield ''.join(x)

def verify_property(x):
    b = True
    b = b and int(x[1] + x[2] + x[3]) % 2 == 0
    b = b and int(x[2] + x[3] + x[4]) % 3 == 0
    b = b and int(x[3] + x[4] + x[5]) % 5 == 0
    b = b and int(x[4] + x[5] + x[6]) % 7 == 0
    b = b and int(x[5] + x[6] + x[7]) % 11 == 0
    b = b and int(x[6] + x[7] + x[8]) % 13 == 0
    b = b and int(x[7] + x[8] + x[9]) % 17 == 0
    return b

if __name__ == '__main__':
    assert(verify_property('1406357289'))
    print(sum(int(x) for x in gen_pandigital() if verify_property(x)))
