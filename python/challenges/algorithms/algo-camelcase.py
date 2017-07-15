"""
Alice wrote a sequence of words in CamelCase as a
string of letters, , having the following properties:

It is a concatenation of one or more words consisting
of English letters.

All letters in the first word are lowercase.

For each of the subsequent words, the first letter is
uppercase and rest of the letters are lowercase.

Given , print the number of words in  on a new line.

Sample Input: saveChangesInTheEditor
Sample Output: 5
"""


def number_of_words(s):
    """
    >>> assert(number_of_words(None) == 0)
    >>> assert(number_of_words('') == 0)
    >>> assert(number_of_words('save') == 1)
    >>> assert(number_of_words('saveChanges') == 2)
    >>> assert(number_of_words('saveChangesInTheEditor') == 5)
    """
    if s is None or len(s) == 0:
        return 0

    return 1 + len([l for l in s if l.isupper()])

val = input().strip()
print(number_of_words(val))
