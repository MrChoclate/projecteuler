"""
Factorial digit sum
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def fac(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

if __name__ == '__main__':
    assert(sum(int(c) for c in str(fac(10))) == 27)
    print(sum(int(c) for c in str(fac(100))))
