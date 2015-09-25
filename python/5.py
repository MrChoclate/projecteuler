"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

import operator
import functools
import math
problem3 = __import__('3')

def prod(iterable):
    return functools.reduce(operator.mul, iterable, 1)

def smallest(limit):
    prime_list = problem3.get_prime_list(limit)
    max_power = [math.floor(math.log(limit) / math.log(p)) for p in prime_list]
    max_power = [p ** x for p, x in zip(prime_list, max_power)]
    return prod(max_power)

if __name__ == '__main__':
    assert(smallest(10) == 2520)
    print(smallest(20))
