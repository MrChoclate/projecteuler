"""
Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import functools
import math

@functools.lru_cache(maxsize=None)
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

def is_curious(x):
    x_ = str(x)
    return sum(fact(int(c)) for c in x_) == x

if __name__ == '__main__':
    assert(is_curious(145))

    # Find upper limit
    sum_, i = fact(9), 1
    while math.log(sum_) / math.log(10) > i:
        i += 1
        sum_ += fact(9)
    print(sum(i for i in range(3, sum_) if is_curious(i)))
