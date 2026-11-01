from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
d = [-1] * (n + 1)
q = deque([1])

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
d[1] = 0

while q:
    u = q.popleft()
    for v in g[u]:
        if d[v] != -1:
            continue
        # 큐에 넣을 때 거리와 방문 여부 기록
        d[v] = d[u] + 1
        q.append(v)

print(d[n])
