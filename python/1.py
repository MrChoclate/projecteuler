"""
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import itertools

def gen(limit=None):
    res = 0
    cycle = [3, 2, 1, 3, 1, 2, 3]
    for i in itertools.cycle(cycle):
        res += i
        if limit and res >= limit:
            break
        yield res
        
if __name__ == '__main__':
    assert(sum(gen(limit=10)) == 23)
    print(sum(gen(limit=1000)))
