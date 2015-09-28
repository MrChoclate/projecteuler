"""
Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

get_prime_list = __import__('3').get_prime_list
is_prime = __import__('3').is_prime

def does_sum_exists(length, prime_list):
    set_ = set(prime_list)
    s = sum(prime_list[:length])
    i = length
    while s < prime_list[-1] and i < len(prime_list):
        if s in set_:
            return s
        s = s - prime_list[i - length] + prime_list[i]
        i += 1
    return False

def find_max_sum(prime_list, limit=100):
    l = []
    for i in range(limit):
        s = does_sum_exists(i, prime_list)
        if s:
            l.append((i, s))
    return max(l)[1]

if __name__ == '__main__':
    assert(find_max_sum(get_prime_list(10 ** 3)) == 953)
    prime_list = get_prime_list(10 ** 6)

    # Calculate upper limit
    s, i = 0, 0
    while s < 10 ** 6:
        s += prime_list[i]
        i += 1

    print(find_max_sum(prime_list, limit=i))
