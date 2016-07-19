import math


def find():
    i = 1
    s = 0
    count = None
    while count != 0:
        count = len([x for x in map(lambda x: x**i, range(1, 10)) if math.ceil(math.log10(x)) == i])
        print(i, [x for x in map(lambda x: x**i, range(1, 10)) if math.ceil(math.log10(x)) == i])
        i += 1
        s += count

    return s

if __name__ == '__main__':
    print(find())  # Do not forget 1 ** 1 = 1
