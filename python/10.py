"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

problem3 = __import__('3')

if __name__ == '__main__':
    prime_list = problem3.get_prime_list
    assert(sum(p for p in prime_list(10) if p < 10) == 17)
    print(sum(prime_list(2 * 10 ** 6)))
