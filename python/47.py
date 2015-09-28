"""
Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
"""

import math

def is_prime(x, prime_list):
    for n in prime_list:
        if n > math.sqrt(x):
            return True
        if x % n == 0:
            return False

save = {}
def decompose(x, prime_list):
    global save  # cache without prime_list
    if x in save:
        return save[x]

    old_x = x
    d = {}
    for p in prime_list:
        if x == 1:
            break
        while x % p == 0:
            if x in save:  # cache hit
                for k, v in save[x].items():
                    d[k] = d.get(k, 0) + 1
                save[old_x] = d
                return d

            d[p] = d.get(p, 0) + 1
            x = x // p
    save[old_x] = d
    return d

def gen_consecutive(nb):
    prime_list = [2, 3, 5, 7]

    i = 1
    tuple_ = [i + k for k in range(nb)]
    while any(len(decompose(x, prime_list)) < nb for x in tuple_):
        tuple_ = [i + 1 for i in tuple_]
        last = prime_list[-1]
        while tuple_[-1] > last:  # prime_list is not big enough
            last += 2
            if is_prime(last, prime_list):
                prime_list.append(last)

    return tuple_[0]

if __name__ == '__main__':
    assert(gen_consecutive(2) == 14)
    assert(gen_consecutive(3) == 644)
    print(gen_consecutive(4))
