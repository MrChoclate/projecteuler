import math


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

def odd_period(N):
    count = 0
    for i in range(N+1):
        if int(math.sqrt(i)) != math.sqrt(i):
            a0, p = decompose(i)
            if len(p) % 2 == 1:
                count += 1
    return count

if __name__ == '__main__':
    print(odd_period(10000))
