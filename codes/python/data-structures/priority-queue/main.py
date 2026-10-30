import heapq

n = int(input())
lst = list(map(int, input().split()))
heap = []
ans = []

for x in lst:
    heapq.heappush(heap, x)

while heap:
    ans.append(heapq.heappop(heap))

print(*ans)
