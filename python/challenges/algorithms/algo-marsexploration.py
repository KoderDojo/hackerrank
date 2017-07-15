"""
Sami's spaceship crashed on Mars! She sends n sequential
SOS messages to Earth for help. Letters in some of the
SOS messages are altered by cosmic radiation during transmission.
Given the signal received by Earth as a string, , determine
how many letters of Sami's SOS have been changed by radiation.

Input Format: There is one line of input: a single string, S.
Letters will always be in all CAPS and a multiple of 3.

Output Format: Print the number of letters in Sami's message
that were altered by cosmic radiation.

Sample Input: SOSSPSSQSSOR
Sample Output: 3
"""


def number_of_differences(str1, str2):
    """
    >>> str1 = str2 = 'ABABABABAB'
    >>> assert(number_of_differences(str1, str2) == 0)
    >>> str1, str2 = 'ABABABABAB', 'BABABABABA'
    >>> assert(number_of_differences(str1, str2) == 10)
    >>> str1, str2 = 'SOSSPSSQSSOR', 'SOSSOSSOSSOS'
    >>> assert(number_of_differences(str1, str2) == 3)
    """
    return sum(str1[i] != str2[i] for i in range(len(str1)))


received_signal = input().strip()
expected_signal = 'SOS' * (len(received_signal) // 3)

print(number_of_differences(received_signal, expected_signal))
