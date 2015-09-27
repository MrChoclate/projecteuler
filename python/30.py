"""
Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""

def is_sum_power(x, p):
    return x == sum(int(c) ** p for c in str(x))

def find_all(power, limit):
    for i in range(2, limit):
        if is_sum_power(i, power):
            yield i

if __name__ == '__main__':
    assert(is_sum_power(1634, 4))
    assert(is_sum_power(8208, 4))
    assert(is_sum_power(9474, 4))
    assert(sum(i for i in find_all(4, 10000)) == 19316)

    # Calculate upper limit
    sum_, digits = 9 ** 5, 9
    while sum_ > digits:
        sum_ += sum_
        digits = digits * 10 + 9
    print(sum(i for i in find_all(5, sum_)))
