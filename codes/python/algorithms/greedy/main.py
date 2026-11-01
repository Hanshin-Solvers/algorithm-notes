n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
cnt = 0
end = 0

# 종료 시각 순서로 정렬
lst.sort(key=lambda x: x[1])
for s, e in lst:
    if s >= end:
        cnt += 1
        end = e

print(cnt)
