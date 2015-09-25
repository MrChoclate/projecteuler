"""
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""

import inflect
_p = inflect.engine()

def get_nb_letters(number):
    return len([c for c in _p.number_to_words(number) if 'a' <= c <= 'z'])

if __name__ == '__main__':
    assert(sum(get_nb_letters(i) for i in range(1, 6)) == 19)
    assert(get_nb_letters(342) == 23)
    assert(get_nb_letters(115) == 20)
    print(sum(get_nb_letters(i) for i in range(1, 1001)))
