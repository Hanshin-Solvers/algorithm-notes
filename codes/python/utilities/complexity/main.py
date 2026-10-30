n = int(input())
cnt = 0
pairs = 0

# N번 실행
for i in range(1, n + 1):
    cnt += 1

# (N - 1) + (N - 2) + ... + 1번 실행
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        pairs += 1

print(cnt)
print(pairs)
