n, q = map(int, input().split())
lst = list(map(int, input().split()))
p = [0] * (n + 1)

for i, x in enumerate(lst, 1):
    p[i] = p[i - 1] + x
for _ in range(q):
    l, r = map(int, input().split())
    print(p[r] - p[l - 1])
