N = 10000
p = list(range(N + 1))
sz = [1] * (N + 1)


def find(x):
    while p[x] != x:
        p[x] = p[p[x]]  # 경로 절반 압축
        x = p[x]
    return x


# Union by Size: 집합의 원소 수를 기준으로 합침
def unite(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if sz[a] < sz[b]:
        a, b = b, a
    p[b] = a
    sz[a] += sz[b]  # 합친 집합의 원소 수 갱신


n, q = map(int, input().split())

for _ in range(q):
    cmd = input().split()
    op = cmd[0]
    a = int(cmd[1])

    if op == "size":
        print(sz[find(a)])
    elif op == "union":
        unite(a, int(cmd[2]))
    else:
        b = int(cmd[2])
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
