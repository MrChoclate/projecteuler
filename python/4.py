"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import itertools

def is_palindrome(number):
    return str(number) == ''.join(reversed(str(number)))

def get_all_number(nb_digits):
    for digits_list in itertools.product(range(10), repeat=nb_digits):
        number = 0
        for i, digit in enumerate(digits_list):
            number += digit * 10 ** i
        yield number

def get_palidromes(nb_digits):
    for x, y in itertools.product(get_all_number(nb_digits), repeat=2):
        if is_palindrome(x * y):
            yield x * y

if __name__ == '__main__':
    assert(is_palindrome(9009))
    assert(max(get_palidromes(2)) == 9009)
    print(max(get_palidromes(3)))
