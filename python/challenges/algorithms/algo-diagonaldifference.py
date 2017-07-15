"""
Given a square matrix of size N x N, calculate the absolute
difference between the sums of its diagonals.

Input Format

The first line contains a single integer, N. The next N lines
denote the matrix's rows, with each line containing
space-separated integers describing the columns.

Output Format

Print the absolute difference between the two sums of the matrix's
diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12

Sample Output

15
"""


def diagonal_difference(matrix):
    n = len(matrix)

    sum_diag1 = sum([matrix[a][a] for a in range(n)])
    sum_diag2 = sum([matrix[a][n-1-a] for a in range(n)])

    return abs(sum_diag1 - sum_diag2)


# create matrix
n = int(input().strip())
m = [list(map(int, input().split(' '))) for i in range(n)]

print(diagonal_difference(m))
