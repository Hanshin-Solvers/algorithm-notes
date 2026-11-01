def dfs(u):
    # 다른 정점으로 이동하기 전에 방문을 표시하여 사이클의 재방문 방지
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
    # 미방문 정점에서 시작한 DFS 하나가 연결 요소 하나를 탐색함
    if not seen[u]:
        cnt += 1
        dfs(u)

print(cnt)
