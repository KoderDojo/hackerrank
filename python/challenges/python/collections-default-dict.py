from collections import defaultdict


n, m = map(int, input().strip().split(' '))
a = defaultdict(list)
b = []

for i in range(n):
    char = input().strip()
    a[char].append(str(i+1))

for j in range(m):
    b.append(input().strip())

for k in b:
    print(' '.join(a[k]) if k in a else -1)
