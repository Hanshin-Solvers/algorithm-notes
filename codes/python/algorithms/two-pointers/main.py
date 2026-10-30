n, target = map(int, input().split())
lst = list(map(int, input().split()))
l = 0
s = 0
ans = n + 1

for r, x in enumerate(lst):
    s += x
    while s >= target:
        ans = min(ans, r - l + 1)
        s -= lst[l]
        l += 1

print(0 if ans == n + 1 else ans)
