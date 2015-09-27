"""
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes
for the consecutive values n = 0 to 79. The product of the coefficients, −79
and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with
n = 0.
"""
import itertools
problem3 = __import__('3')
get_prime_list = problem3.get_prime_list

def quadratic_expression(n, a, b):
    return n * n + a * n + b

def score(a, b, prime_list):
    x, i = quadratic_expression(0, a, b), 0
    while x in prime_list:
        i += 1
        x = quadratic_expression(i, a, b)
    return i

if __name__ == '__main__':
    # quadratic_expression cannot exceed 2001000
    list_ = set(get_prime_list(2001000))
    assert(score(1, 41, list_) == 40)
    assert(score(-79, 1601, list_) == 80)

    bs = [prime for prime in list_ if prime < 1000]
    bs += [- prime for prime in bs]
    comb = itertools.product(range(-999, 1000, 2), bs)
    print(max((score(a, b, list_), a * b) for a, b in comb))
