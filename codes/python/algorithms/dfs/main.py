def dfs(u):
    seen[u] = True
    for v in g[u]:
        if not seen[v]:
            dfs(v)


n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
seen = [False] * (n + 1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for u in range(1, n + 1):
    if not seen[u]:
        cnt += 1
        dfs(u)

print(cnt)
