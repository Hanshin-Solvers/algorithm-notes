INF = 1000000
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
d = [INF] * (n + 1)
d[1] = 0
cycle = False

for i in range(1, n + 1):
    changed = False
    for a, b, w in edges:
        # 시작점에서 도달한 정점의 간선만 사용
        if d[a] == INF:
            continue
        if d[a] + w < d[b]:
            d[b] = d[a] + w
            changed = True
            # n번째 반복에도 갱신되면 시작점에서 도달 가능한 음수 사이클 존재
            if i == n:
                cycle = True
    # 거리 변화가 없으면 이후 반복에서도 갱신되지 않으므로 종료
    if not changed:
        break

if cycle:
    print("NEGATIVE CYCLE")
else:
    print(*["INF" if x == INF else x for x in d[1:]])
