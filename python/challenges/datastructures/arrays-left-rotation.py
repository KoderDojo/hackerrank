"""
Given an array of  integers and a number, n, perform d left rotations
on the array. Then print the updated array as a single line of
space-separated integers.
"""


_, d = map(int, input().strip().split(' '))
arr = input().strip().split(' ')

shifted_arr = arr[d:] + arr[0:d]
print(' '.join(shifted_arr))
