"""
Given an array of integers, calculate which fraction of its
elements are positive, which fraction of its elements are
negative, and which fraction of its elements are zeroes,
respectively. Print the decimal value of each fraction on a
new line.

Sample Input
    6
    -4 3 -9 0 4 1

Sample Output
    0.500000
    0.333333
    0.166667
"""


n, values = int(input()), tuple(map(int, input().strip().split(' ')))

positives = len(tuple(filter(lambda v: v > 0, values)))
zeros = len(tuple(filter(lambda v: v == 0, values)))
negatives = n - positives - zeros

print('{0:.6f}'.format(positives / n))
print('{0:.6f}'.format(negatives / n))
print('{0:.6f}'.format(zeros / n))
