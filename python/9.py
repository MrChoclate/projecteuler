"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def gen_numbers(n):
    for a in range(n):
        for b in range(a + 1, n):
            c = 1000 - a - b
            if a < b < c:
                yield a, b, 1000 - a - b

def is_pythagorean(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

if __name__ == '__main__':
    for a, b, c in gen_numbers(1000):
        if sum((a, b, c)) == 1000 and is_pythagorean(a, b, c):
            print(a * b * c)
