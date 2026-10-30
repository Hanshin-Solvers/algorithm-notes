def dfs(u, par):
    # 자식 탐색 전 부모와 크기 초기값 설정
    p[u] = par
    sz[u] = 1
    for v in g[u]:
        if v == par:
            continue
        d[v] = d[u] + 1
        dfs(v, u)
        # 자식 탐색 후 서브트리 크기 합산
        sz[u] += sz[v]


n = int(input())
g = [[] for _ in range(n + 1)]
p = [0] * (n + 1)
d = [0] * (n + 1)
sz = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dfs(1, 0)

for i in range(1, n + 1):
    print(p[i], d[i], sz[i])
