def dfs(x):
    seen[x] = True

    # 연산 결과가 범위 안이고 미방문 상태이면 탐색
    if x + 1 <= 100 and not seen[x + 1]:
        dfs(x + 1)
    if x * 2 <= 100 and not seen[x * 2]:
        dfs(x * 2)


a, b = map(int, input().split())
seen = [False] * 101

dfs(a)
if seen[b]:
    print('YES')
else:
    print('NO')
