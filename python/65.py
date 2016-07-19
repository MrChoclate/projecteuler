"""
Convergents of e
Problem 65

The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates
that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for
square roots provide the best rational approximations. Let us consider the
convergents for √2.

...


Hence the sequence of the first ten convergents for √2 are:
1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.

"""
from fractions import Fraction

def get_e(n):
    return 2, [1 if (i % 3 != 1) else 2 * (1 + (i - 1) // 3) for i in range(n)]

def get_convergent(a0, p, N):
    if N == 1:
        return Fraction(a0, 1)
    return Fraction(a0, 1) + Fraction(1, get_convergent(p[0], p[1:], N-1))


if __name__ == '__main__':
    print(sum(map(int, str(get_convergent(*get_e(100), 100).numerator))))
