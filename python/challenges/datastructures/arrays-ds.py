"""
Given an array, , of  integers, print each element in reverse
order as a single line of space-separated integers.
"""
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(' '.join(map(str, arr[::-1])))
