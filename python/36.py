"""
Double-base palindromes
Problem 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""



def is_palindrome(x):
    return x == ''.join(reversed(x))

def is_double_palindrome(x):
    return is_palindrome(str(x)) and is_palindrome(bin(x)[2:])

if __name__ == '__main__':
    assert(is_double_palindrome(585))
    print(sum(i for i in range(10 ** 6) if is_double_palindrome(i)))
