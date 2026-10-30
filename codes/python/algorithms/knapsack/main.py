n, limit = map(int, input().split())
dp = [0] * (limit + 1)
un = [0] * (limit + 1)

for _ in range(n):
    w, v = map(int, input().split())
    # 큰 용량부터 갱신하여 같은 물건의 중복 선택 방지
    for c in range(limit, w - 1, -1):
        dp[c] = max(dp[c], dp[c - w] + v)
    # 작은 용량부터 갱신하여 같은 종류를 다시 선택
    for c in range(w, limit + 1):
        un[c] = max(un[c], un[c - w] + v)

print(dp[limit])
print(un[limit])
