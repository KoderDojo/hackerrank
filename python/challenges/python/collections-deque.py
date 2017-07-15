from collections import deque


d = deque()
num = int(input().strip())
for i in range(num):
    cmd, *arg = input().strip().split()
    if len(arg) == 0:
        eval(f'd.{cmd}()')
    else:
        eval(f'd.{cmd}({arg[0]})')

print(' '.join(str(i) for i in d))
