from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
c = [-1] * (n + 1)
q = deque()
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ok = True
for i in range(1, n + 1):
    if c[i] != -1:
        continue
    c[i] = 0
    q.append(i)
    while q:
        u = q.popleft()
        for v in g[u]:
            if c[v] == -1:
                c[v] = 1 - c[u]
                q.append(v)
            elif c[v] == c[u]:
                ok = False

print("YES" if ok else "NO")
