n, k = map(int, input().split())
lst = list(map(int, input().split()))
l, r = 1, max(lst)
ans = 0

while l <= r:
    m = (l + r) // 2
    cnt = sum(x // m for x in lst)
    if cnt >= k:
        ans = m
        l = m + 1
    else:
        r = m - 1

print(ans)
