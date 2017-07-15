"""
Julius Caesar protected his confidential information by
encrypting it in a cipher. Caesar's cipher rotated every
letter in a string by a fixed number, , making it unreadable
by his enemies. Given a string, S, and a number, K, encrypt
S and print the resulting string.

Sample Input: 11, middle-Outz, 2

Sample Output: okffng-Qwvb
"""


def encrypt_letter(letter, shift):
    """
    >>> assert(encrypt_letter('a', 0) == 'a')
    >>> assert(encrypt_letter('a', 3) == 'd')
    >>> assert(encrypt_letter('z', 3) == 'c')
    >>> assert(encrypt_letter('a', 26) == 'a')
    >>> assert(encrypt_letter('b', 26) == 'b')
    >>> assert(encrypt_letter('A', 0) == 'A')
    >>> assert(encrypt_letter(' ', 123) == ' ')
    """

    val = ord(letter)

    if 64 < val < 91:
        return chr(65 + (val - 65 + shift) % 26)
    elif 96 < val < 123:
        return chr(97 + (val - 97 + shift) % 26)
    else:
        return letter


n, message, num_shift = int(input()), input().strip(), int(input().strip())
print(''.join(map(encrypt_letter, message, [num_shift]*n)))
