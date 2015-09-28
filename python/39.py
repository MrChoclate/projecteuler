"""
Integer right triangles
Problem 39

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

def nb_solutions(p):
    res = 0
    for a in range(1, p):
        for b in range(a, p):
            c = p - a - b
            if a * a + b * b == c * c:
                res += 1
    return res

if __name__ == '__main__':
    assert(nb_solutions(120) == 3)
    print(max((nb_solutions(p), p) for p in range(1001))[1])
