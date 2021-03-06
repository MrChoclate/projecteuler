"""
Triangular, pentagonal, and hexagonal
Problem 45

Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:
Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	Hn=n(2n−1) 	  	    1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

import math

def is_pentagonal(x):
    return math.sqrt(24 * x + 1).is_integer() and math.sqrt(24 * x + 1) % 6 == 5

def is_triangle(x):
    return math.sqrt(8 * x + 1).is_integer()

def gen_hexagonal():
    i = 144
    while True:
        yield i * (2 * i - 1)
        i += 1

if __name__ == '__main__':
    assert(is_pentagonal(40755))
    assert(is_triangle(40755))
    for x in gen_hexagonal():
        if is_pentagonal(x) and is_triangle(x):
            print(x)
            break
