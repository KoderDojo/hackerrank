# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with
# the element type float.
#
# Input:  1 2 3 4 -8 -10
# Output: [-10.  -8.   4.   3.   2.   1.]


import numpy as np


print(np.flipud(np.array(input().split(' '), float)))
