"""
Steve has a string, , consisting of  lowercase English alphabetic
letters. In one operation, he can delete any pair of adjacent
letters with same value. For example, string "aabcc" would become
either "aab" or "bcc" after operation.

Steve wants to reduce  as much as possible. To do this, he will
repeat the above operation as many times as it can be performed.
Help Steve out by finding and printing 's non-reducible form!

Note: If the final string is empty, print Empty String.

Sample Input: aaabccddd
Sample Output: abd
"""


def reduce_string(s):
    """
    >>> assert(reduce_string(None) == 'Empty String')
    >>> assert(reduce_string('') == 'Empty String')
    >>> assert(reduce_string('abc') == 'abc')
    >>> assert(reduce_string('aabbc') == 'c')
    >>> assert(reduce_string('abcc') == 'ab')
    >>> assert(reduce_string('aabbcc') == 'Empty String')
    """
    if s is None or len(s) == 0:
        return 'Empty String'

    stack = []

    for char in s:
        if len(stack) == 0:
            stack.append(char)
            continue

        if char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    return 'Empty String' if len(stack) == 0 else ''.join(stack)
