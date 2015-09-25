"""
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less
than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

def proper_divisors(x):
    return [i for i in range(1, x) if x % i == 0]

def is_abundant(x):
    return sum(proper_divisors(x)) > x

def get_abundant_numbers():
    return {x: True for x in range(1, 28123) if is_abundant(x)}

def is_sum(x, abundant_numbers):
    for i in range(12, x):
        if i in abundant_numbers and x - i in abundant_numbers:
            return True
    return False


if __name__ == '__main__':
    assert(is_abundant(12) and not is_abundant(10))
    abundant_numbers = get_abundant_numbers()
    assert(is_sum(24, abundant_numbers) and not is_sum(23, abundant_numbers))
    print('done')
    print(sum(i for i in range(1, 28123) if not is_sum(i, abundant_numbers)))
