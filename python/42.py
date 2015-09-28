"""
Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""

def compute_triangles(n):
    l, res = [], 0
    for i in range(1, n):
        res += i
        l.append(res)
    return set(l)

def is_triangle_word(w, triangles):
    return sum(ord(c) - ord('A') + 1 for c in w) in triangles

if __name__ == '__main__':
    with open('p042_words.txt') as f:
        words = ''.join(line for line in f)
    words = [w.strip('""') for w in words.split(',')]
    triangles = compute_triangles(30)
    assert(is_triangle_word('SKY', triangles))
    print(len([w for w in words if is_triangle_word(w, triangles)]))
