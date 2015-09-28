"""
Pandigital multiples
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def make_number(x, tuple_):
    return ''.join(str(x * i) for i in tuple_)

def gen_pandigital_multiples():
    for i in range(3, 11):
        tuple_ = tuple(range(1, i))
        res, i = '', 1
        while len(res) <= 9:
            res = make_number(i, tuple_)
            if len(res) == 9 and set(res) == set('123456789'):
                yield res
            i += 1

if __name__ == '__main__':
    print(max(gen_pandigital_multiples()))
