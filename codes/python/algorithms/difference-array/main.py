n, q = map(int, input().split())
d = [0] * (n + 2)
lst = []
s = 0

for _ in range(q):
    l, r, x = map(int, input().split())
    d[l] += x
    d[r + 1] -= x
for i in range(1, n + 1):
    s += d[i]
    lst.append(s)

print(*lst)
