s = input()
p = input()
n = len(s)
m = len(p)
ans = []

for i in range(n - m + 1):
    j = 0
    while j < m and s[i + j] == p[j]:
        j += 1
    if j == m:
        ans.append(i)

print(len(ans))
print(*ans)
