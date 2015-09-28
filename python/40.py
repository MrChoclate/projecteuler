"""
Champernowne's constant
Problem 40

An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def gen_champernowne(limit=None):
    i = 1
    while not limit or i <= limit:
        for c in str(i):
            yield int(c)
        i += 1

if __name__ == '__main__':
    assert(list(gen_champernowne(100))[13] == 1)
    i = res = next_ = 1
    for c in gen_champernowne():
        if i % next_ == 0:
            res *= c
            next_ *= 10
        if next_ > 1000000:
            break
        i += 1
    print(res)
