"""
Cubic permutations
Problem 62

The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104
 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has
 exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
"""

def find():
    d = {}
    i = 1
    while True:
        val = "".join(sorted(str(i ** 3)))
        d[val] = d.get(val, []) + [i ** 3]
        i += 1
        if len(d[val]) == 5:
            print(d[val][0])
            break

if __name__ == '__main__':
    find()
