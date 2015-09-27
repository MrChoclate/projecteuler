"""
Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""

def solve(size):
    assert(size % 2 == 1)
    size = (size - 1) // 2
    res = count = 1
    delta = 0
    for _ in range(size):
        delta += 2
        for _ in range(4):
            count += delta
            res += count
    return res

if __name__ == '__main__':
    assert(solve(5) == 101)
    print(solve(1001))
