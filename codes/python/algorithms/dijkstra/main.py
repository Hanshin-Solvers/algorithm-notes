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
    # 더 짧은 경로로 이미 갱신된 정점의 오래된 큐 항목 제외
    if du != d[u]:
        continue
    for v, w in g[u]:
        # u를 거쳐 더 짧아지면 거리와 경로 복원용 이전 정점 갱신
        if du + w < d[v]:
            d[v] = du + w
            p[v] = u
            heapq.heappush(heap, (d[v], v))

if d[t] == INF:
    print(-1)
else:
    # 도착점에서 이전 정점을 따라가며 경로를 역순으로 수집
    u = t
    while u != 0:
        ans.append(u)
        u = p[u]
    ans.reverse()
    print(d[t])
    print(*ans)
