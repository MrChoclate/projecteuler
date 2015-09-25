"""
Power digit sum
Problem 16

2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ** 1000?
"""

def solve(power):
    s = str(2 ** power)
    return sum(int(c) for c in s)

if __name__ == '__main__':
    assert(solve(15) == 26)
    print(solve(1000))
