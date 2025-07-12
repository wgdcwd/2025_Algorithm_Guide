import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []
for i in list(map(int, input().split())):
    heapq.heappush(heap, i)

for _ in range(n - 1):
    for i in list(map(int, input().split())):
        heapq.heappush(heap, i)

    for i in range(n):
        heapq.heappop(heap)

print(heapq.heappop(heap))
