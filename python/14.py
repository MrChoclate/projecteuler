"""
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import functools

def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

save = {1: 1}
def len_collatz(n):
    ini, stack = n, []
    while n != 1:
        if n in save:
            break

        stack.append((n, collatz(n)))
        n = collatz(n)

    while(stack):
        x, y = stack.pop()
        save[x] = save[y] + 1

    return save[ini]

if __name__ == '__main__':
    assert(len_collatz(13) == 10)
    lens = [len_collatz(i) for i in range(1, 10 ** 6 + 1)]
    print(lens.index(max(lens)) + 1)
