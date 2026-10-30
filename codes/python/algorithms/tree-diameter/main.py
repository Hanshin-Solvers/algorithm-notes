def dfs(u, par, dist):
    global far, best

    if dist > best:
        best = dist
        far = u
    for v, w in g[u]:
        if v == par:
            continue
        dfs(v, u, dist + w)


n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
    g[b].append((a, w))

far = 1
best = 0
dfs(1, 0, 0)
a = far
best = 0
dfs(a, 0, 0)

print(best)
