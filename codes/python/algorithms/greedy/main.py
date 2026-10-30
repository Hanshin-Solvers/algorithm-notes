n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
cnt = 0
end = 0
merged = []

for s, e in sorted(lst, key=lambda x: x[1]):
    if s >= end:
        cnt += 1
        end = e

# 시작점 순서로 구간 병합
for s, e in sorted(lst):
    if not merged or merged[-1][1] < s:
        merged.append([s, e])
    else:
        merged[-1][1] = max(merged[-1][1], e)

print(cnt)
print(len(merged))
for s, e in merged:
    print(s, e)
