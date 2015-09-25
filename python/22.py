"""
Names scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def name_score(name):
    return sum((ord(c) - ord('A') + 1) for c in name)

def total_score(names):
    res = 0
    for i, name in enumerate(names):
        res += (i + 1) * name_score(name)
    return res

if __name__ == '__main__':
    assert(name_score('COLIN') == 53)
    with open('p022_names.txt') as f:
        data = ''.join(line for line in f)
    names = [name.strip(' "') for name in data.split(',')]
    print(total_score(sorted(names)))
