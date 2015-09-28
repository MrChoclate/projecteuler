"""
Goldbach's other conjecture
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""

import math

def is_prime(x, prime_list):
    for n in prime_list:
        if n > math.sqrt(x):
            return True
        if x % n == 0:
            return False

def is_goldbach_right(x, prime_list):
    return any(math.sqrt((x - p) / 2).is_integer() for p in prime_list)

def solve():
    list_ = [2, 3]

    last = list_[-1]
    while True:
        last += 2
        if is_prime(last, list_):
            list_.append(last)
        elif not is_goldbach_right(last, list_):
            return last

if __name__ == '__main__':
    print(solve())
