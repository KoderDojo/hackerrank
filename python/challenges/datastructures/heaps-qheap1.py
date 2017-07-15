import heapq


heap = []
n = int(input().strip())
for _ in range(n):
    cmd, *args = input().strip().split(' ')
    if cmd == "1":
        heapq.heappush(heap, int(args[0]))
    elif cmd == "2":
        item = int(args[0])
        heap.remove(item)
        heapq.heapify(heap)
    else:
        print(heapq.nsmallest(1, heap)[0])
