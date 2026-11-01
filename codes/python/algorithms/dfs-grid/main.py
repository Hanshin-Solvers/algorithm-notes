def dfs(r, c):
    seen[r][c] = True

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        # 범위 확인 후 벽과 방문 여부 확인
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if g[nr][nc] == 0 or seen[nr][nc]:
            continue
        dfs(nr, nc)


n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
seen = [[False] * m for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 0

for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and not seen[i][j]:
            # 새 영역 탐색
            cnt += 1
            dfs(i, j)

print(cnt)
