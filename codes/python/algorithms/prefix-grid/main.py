n, m, q = map(int, input().split())
p = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j, x in enumerate(row, 1):
        # 위쪽 합과 왼쪽 합에서 두 번 포함된 왼쪽 위 영역을 한 번 뺌
        p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + x
for _ in range(q):
    a, b, c, d = map(int, input().split())
    # 큰 직사각형에서 위·왼쪽 영역을 빼고 두 번 빠진 공통 영역을 더함
    print(p[c][d] - p[a - 1][d] - p[c][b - 1] + p[a - 1][b - 1])
