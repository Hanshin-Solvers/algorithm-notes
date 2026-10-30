INF = 1000000
n, m = map(int, input().split())
d = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    d[i][i] = 0
for _ in range(m):
    a, b, w = map(int, input().split())
    d[a][b] = min(d[a][b], w)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if d[i][k] == INF or d[k][j] == INF:
                continue
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for row in d[1:]:
    print(*[-1 if x == INF else x for x in row[1:]])
