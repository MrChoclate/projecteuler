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
