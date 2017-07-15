from collections import Counter


_, shoes = input(), dict(Counter(map(int, input().strip().split(' '))))
total_requests = int(input().strip())

total_amount = 0
for i in range(total_requests):
    size, amount = map(int, input().strip().split(' '))

    if shoes.get(size, 0) > 0:
        shoes[size] -= 1
        total_amount += amount

print(total_amount)
