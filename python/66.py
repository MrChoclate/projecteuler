import math
from fractions import Fraction


def decompose(x):
    done = set()
    a0 = math.floor(math.sqrt(x))
    dem = 1
    rem = -a0
    p = []

    while True:
        dem = (x - rem ** 2) // dem
        a = math.floor((math.sqrt(x) - rem) / dem)
        rem =  - rem - dem * a
        if (dem, rem) in done:
            break
        done.add((dem, rem))
        p.append(a)

    return a0, p


def get_convergent(a0, p, N):
    if N == 1:
        return Fraction(a0, 1)
    return Fraction(a0, 1) + Fraction(1, get_convergent(p[(N - 2) % len(p)], p, N-1))


def is_square(x):
    return int(math.sqrt(x)) == math.sqrt(x)

def solve_D(D):
    if is_square(D):
        return 0

    a0, p = decompose(D)
    N = 1
    f = get_convergent(a0, p, N)
    while f.numerator ** 2 - D * f.denominator ** 2 != 1:
        N += 1
        f = get_convergent(a0, p, N)

    return f.numerator

if __name__ == '__main__':
    print(max((solve_D(i), i) for i in range(2, 1000 + 1)))
