def get_with_formula(f):
    i = 1
    while len(str(f(i))) < 4:
        i += 1

    d = {}
    while len(str(f(i))) == 4:
        d[str(f(i))[:2]] = d.get(str(f(i))[:2], []) + [str(f(i))]
        i += 1

    return d

def get_triangle():
    return get_with_formula(lambda n: int(n * (n + 1) / 2))

def get_square():
    return get_with_formula(lambda n: int(n * n))

def get_pentagonal():
    return get_with_formula(lambda n: int(n * (3 * n - 1) / 2))

def get_hexagonal():
    return get_with_formula(lambda n: int(n * (2 * n - 1)))

def get_heptagonal():
    return get_with_formula(lambda n: int(n * (5 * n - 3)  / 2))

def get_octagonal():
    return get_with_formula(lambda n: int(n * (3 * n - 2)))

def find(current_sol, remaining):
    if not remaining and current_sol[-1][2:] == current_sol[0][:2]:
        print(sum(map(int, current_sol)))

    end = current_sol[-1][2:]
    for set_ in remaining:
        for number in set_.get(end, []):
            find(current_sol + [number], [x for x in remaining if x != set_])


if __name__ == '__main__':
    t = get_triangle()
    t_ = [x for key, value in t.items() for x in value]
    s = get_square()
    p = get_pentagonal()
    hx = get_hexagonal()
    hp = get_heptagonal()
    o = get_octagonal()

    for number in t_:
        find([number], [s, p, hx, hp, o])
