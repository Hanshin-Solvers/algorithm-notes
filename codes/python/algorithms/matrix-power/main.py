def mul(a, b):
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c


def power(a, b):
    if b == 0:
        t = [[0] * n for _ in range(n)]
        for i in range(n):
            t[i][i] = 1
        return t
    t = power(a, b // 2)
    t = mul(t, t)
    if b % 2 == 1:
        t = mul(t, a)
    return t


n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
t = power(a, b)

for row in t:
    print(*row)
