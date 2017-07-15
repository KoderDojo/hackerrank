"""
Read an integer N. For all non-negative integers i < N,
print i^2. See the sample for details.
"""


n = int(input().strip())
for i in range(n):
    print(i*i)
