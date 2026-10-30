def find(x):
    while x != p[x]:
        p[x] = p[p[x]]
        x = p[x]
    return x


def unite(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    if sz[a] < sz[b]:
        a, b = b, a
    p[b] = a
    sz[a] += sz[b]
    return True


n, m = map(int, input().split())
p = list(range(n + 1))
sz = [1] * (n + 1)
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda e: e[2])
cnt = 0
ans = 0

for a, b, w in edges:
    if unite(a, b):
        ans += w
        cnt += 1

if cnt == n - 1:
    print(ans)
else:
    print("IMPOSSIBLE")
