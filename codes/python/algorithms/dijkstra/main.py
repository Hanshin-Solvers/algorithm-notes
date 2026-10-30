import heapq

INF = 1000000
n, m, s, t = map(int, input().split())
g = [[] for _ in range(n + 1)]
d = [INF] * (n + 1)
p = [0] * (n + 1)
heap = [(0, s)]
ans = []
for _ in range(m):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
d[s] = 0

while heap:
    du, u = heapq.heappop(heap)
    if du != d[u]:
        continue
    for v, w in g[u]:
        if du + w < d[v]:
            d[v] = du + w
            p[v] = u
            heapq.heappush(heap, (d[v], v))

if d[t] == INF:
    print(-1)
else:
    u = t
    while u != 0:
        ans.append(u)
        u = p[u]
    ans.reverse()
    print(d[t])
    print(*ans)
