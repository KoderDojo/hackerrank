from collections import Counter


def is_pangram(s):
    """
    We will assume that there has to be at least
    1 space, because I don't know of a single word
    that is a pangram.

    If this is the case, you can remove all spaces
    and check to see if length is 26. Didn't want to
    waste the clock cycles for kicks.
    """
    if s is None:
        return 'not pangram'

    return 'pangram' if len(Counter(s.lower())) == 27 else 'not pangram'

# assert(is_pangram(None) == 'not pangram')
# assert(is_pangram("We promptly judged antique ivory buckles for the next prize") == 'pangram')
# assert(is_pangram("We promptly judged antique ivory buckles for the prize") == 'not pangram')

val = input().strip()
print(is_pangram(val))
