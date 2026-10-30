INF = 1000000
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
d = [INF] * (n + 1)
d[1] = 0
cycle = False

for i in range(1, n + 1):
    changed = False
    for a, b, w in edges:
        if d[a] == INF:
            continue
        if d[a] + w < d[b]:
            d[b] = d[a] + w
            changed = True
            if i == n:
                cycle = True
    if not changed:
        break

if cycle:
    print("NEGATIVE CYCLE")
else:
    print(*["INF" if x == INF else x for x in d[1:]])
