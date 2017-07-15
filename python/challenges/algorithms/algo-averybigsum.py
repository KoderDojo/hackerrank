"""
You are given an array of integers of size . You need
to print the sum of the elements in the array, keeping
in mind that some of those integers may be quite large.

Input:
    5
    1000000001 1000000002 1000000003 1000000004 1000000005

Output:
    5000000015

"""


_, numbers = input(), tuple(map(int, input().strip().split(' ')))

print(sum(numbers))
