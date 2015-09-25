"""
Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import functools

def has_two_choice(length, x, y):
    return not(x == length or y == length)

@functools.lru_cache(maxsize=None)
def travel(x, y, length):
    if not has_two_choice(length, x, y):
        return 1
    else:
        return travel(x + 1, y, length) + travel(x, y + 1, length)

def nb_path(length):
    return travel(0, 0, length)


if __name__ == '__main__':
    assert(nb_path(2) == 6)
    print(nb_path(20))
