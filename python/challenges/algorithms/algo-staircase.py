"""
Consider a staircase of size 4:

   #
  ##
 ###
####

Observe that its base and height are both equal to , and the image
is drawn using # symbols and spaces. The last line is not preceded
by any spaces.

Write a program that prints a staircase of size N.
"""


class Staircase:
    def __init__(self, size):
        self.size = size

    def __repr__(self):
        result = ''

        for i in range(1, self.size+1):
            result += ' ' * (self.size - i) + '#' * i + '\n'

        return result


n = int(input().strip())
sc = Staircase(n)
print(sc)
