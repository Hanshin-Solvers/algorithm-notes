n, m = map(int, input().split())
g = [input().strip() for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]
# 시작 칸에 도착한 경우 한 가지로 초기화
dp[1][1] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j == 1:
            continue
        # 현재 칸으로 오는 위쪽 경로와 왼쪽 경로의 수를 합침
        if g[i - 1][j - 1] == '1':
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[n][m])
