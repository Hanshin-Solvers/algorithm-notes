INF = 1000000
n, m = map(int, input().split())
d = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    d[i][i] = 0
for _ in range(m):
    a, b, w = map(int, input().split())
    # 같은 두 정점 사이의 여러 간선 중 최소 가중치 저장
    d[a][b] = min(d[a][b], w)

# 경유 가능한 정점을 k까지 확장하므로 k를 가장 바깥에서 순회
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # i에서 k 또는 k에서 j로 갈 수 없으면 경로 결합 제외
            if d[i][k] == INF or d[k][j] == INF:
                continue
            # 기존 거리와 i → k → j 경로의 거리 비교
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for row in d[1:]:
    print(*[-1 if x == INF else x for x in row[1:]])
