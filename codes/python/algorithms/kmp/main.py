s = input()
p = input()
n = len(s)
m = len(p)
pi = [0] * m
ans = []

# 패턴의 접두사 함수 계산
j = 0
for i in range(1, m):
    while j > 0 and p[i] != p[j]:
        j = pi[j - 1]
    if p[i] == p[j]:
        j += 1
    pi[i] = j

# 본문 탐색과 겹치는 일치 처리
j = 0
for i in range(n):
    while j > 0 and s[i] != p[j]:
        j = pi[j - 1]
    if s[i] == p[j]:
        j += 1
    if j == m:
        ans.append(i - m + 1)
        j = pi[j - 1]

print(len(ans))
print(*ans)
