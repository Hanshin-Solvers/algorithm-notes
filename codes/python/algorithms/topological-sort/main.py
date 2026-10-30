import heapq

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
d = [0] * (n + 1)
heap = []
ans = []
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    d[b] += 1
for i in range(1, n + 1):
    if d[i] == 0:
        heapq.heappush(heap, i)

while heap:
    u = heapq.heappop(heap)
    ans.append(u)
    for v in g[u]:
        d[v] -= 1
        if d[v] == 0:
            heapq.heappush(heap, v)

if len(ans) != n:
    print("IMPOSSIBLE")
else:
    print(*ans)
