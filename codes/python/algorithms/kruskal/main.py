def find(x):
    while x != p[x]:
        # 조부모로 연결하여 대표까지의 경로 단축
        p[x] = p[p[x]]
        x = p[x]
    return x


def unite(a, b):
    a = find(a)
    b = find(b)
    # 이미 같은 집합이면 간선 추가 시 사이클이 생기므로 제외
    if a == b:
        return False
    # 작은 집합을 큰 집합 아래에 연결하도록 대표 교환
    if sz[a] < sz[b]:
        a, b = b, a
    p[b] = a
    sz[a] += sz[b]
    return True


n, m = map(int, input().split())
p = list(range(n + 1))
sz = [1] * (n + 1)
edges = [tuple(map(int, input().split())) for _ in range(m)]
# 가중치가 작은 간선부터 검사
edges.sort(key=lambda e: e[2])
cnt = 0
ans = 0

for a, b, w in edges:
    if unite(a, b):
        ans += w
        cnt += 1

# n-1개 간선을 선택했으면 모든 정점을 연결한 신장 트리 완성
if cnt == n - 1:
    print(ans)
else:
    print("IMPOSSIBLE")
