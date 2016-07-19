from fractions import Fraction

def get_e(n):
    return 2, [1 if (i % 3 != 1) else 2 * (1 + (i - 1) // 3) for i in range(n)]

def get_convergent(a0, p, N):
    if N == 1:
        return Fraction(a0, 1)
    return Fraction(a0, 1) + Fraction(1, get_convergent(p[0], p[1:], N-1))


if __name__ == '__main__':
    print(sum(map(int, str(get_convergent(*get_e(100), 100).numerator))))
