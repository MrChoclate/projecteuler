"""
Circular primes
Problem 35

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""

get_prime_list = __import__('3').get_prime_list

def is_circular(x, prime_list):
    x_ = str(x)
    for i in range(len(x_)):
        if int(x_[i:] + x_[:i]) not in prime_list:
            return False
    return True

if __name__ == '__main__':
    prime_list = set(get_prime_list(10 ** 7))
    assert(len(list(x for x in prime_list if x < 100 and is_circular(x, prime_list))) == 13)
    print(len(list(x for x in prime_list if x < 10 ** 6 and is_circular(x, prime_list))))
