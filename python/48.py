"""
Self powers
Problem 48

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

def serie(n):
    return str(sum(pow(i, i, 10 ** 10) for i in range(1, n + 1)))[-10:]

if __name__ == '__main__':
    assert(serie(10) == '405071317')
    print(serie(1000))
