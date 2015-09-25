"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

problem3 = __import__('3')

if __name__ == '__main__':
    assert(problem3.get_prime_list(limit=13)[5] == 13)
    print(problem3.get_prime_list(limit=10**6)[10000])
