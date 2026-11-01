from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * m for _ in range(n)]
q = deque([(0, 0)])
# d[x][y]: 시작 칸에서의 최소 이동 횟수, -1은 미방문
d[0][0] = 0

while q:
    x, y = q.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        # 배열에 접근하기 전에 다음 칸이 격자 안인지 확인
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if g[nx][ny] == 0 or d[nx][ny] != -1:
            continue
        # 처음 발견한 거리가 최단 거리이므로 큐에 넣기 전에 방문 처리
        d[nx][ny] = d[x][y] + 1
        q.append((nx, ny))

print(d[n - 1][m - 1])
