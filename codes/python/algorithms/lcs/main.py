a = input().strip()
b = input().strip()
n, m = len(a), len(b)
# dp[i][j]: 두 문자열의 앞 i개와 앞 j개 문자로 만든 LCS 길이
dp = [[0] * (m + 1) for _ in range(n + 1)]
ans = []

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 문자가 같으면 두 문자열에서 함께 선택
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 마지막 칸에서 문자를 선택하거나 길이가 유지되는 칸으로 이동
i, j = n, m
while i > 0 and j > 0:
    # 문자가 같으면 두 문자열에서 함께 선택
    if a[i - 1] == b[j - 1]:
        ans.append(a[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1
# 뒤에서부터 모은 문자를 뒤집어 원래 순서 복원
ans.reverse()

print(dp[n][m])
print(''.join(ans))
