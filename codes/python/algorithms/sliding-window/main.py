n, k = map(int, input().split())
lst = list(map(int, input().split()))
s = sum(lst[:k])
ans = s

for i in range(k, n):
    s -= lst[i - k]
    s += lst[i]
    ans = max(ans, s)

print(ans)
