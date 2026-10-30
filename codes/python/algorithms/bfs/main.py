from collections import deque

n, m = map(int, input().split())
g = [input().strip() for _ in range(n)]
d = [[-1] * m for _ in range(n)]
q = deque([(0, 0)])
d[0][0] = 0

while q:
    x, y = q.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if g[nx][ny] == '0' or d[nx][ny] != -1:
            continue
        d[nx][ny] = d[x][y] + 1
        q.append((nx, ny))

print(d[n - 1][m - 1])
