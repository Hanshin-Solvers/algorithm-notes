n = int(input())
lst = list(map(int, input().split()))
cur = 0
ans = 0

lst.sort()
for x in lst:
    # 현재 작업의 완료 시각과 전체 합 갱신
    cur += x
    ans += cur

print(ans)
