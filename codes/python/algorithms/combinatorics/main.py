n, r = map(int, input().split())
p = 1
f = 1

for i in range(r):
    p *= n - i
    f *= i + 1

print(p, p // f)
