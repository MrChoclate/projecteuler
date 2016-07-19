"""
Permuted multiples
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.
"""

def verify_property(x):
    b = set(str(x)) == set(str(2 * x)) == set(str(3 * x)) == set(str(4 * x))
    b = b and set(str(4 * x)) == set(str(5 * x)) == set(str(6 * x))
    return b

if __name__ == '__main__':
    i = 1
    while True:
        if verify_property(i):
            break
        i += 1
    print(i)
