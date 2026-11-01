n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
ans = []

# 시작점 순서로 정렬 후 병합
lst.sort()
for s, e in lst:
    if not ans or ans[-1][1] < s:
        ans.append([s, e])
    else:
        ans[-1][1] = max(ans[-1][1], e)

print(len(ans))
for s, e in ans:
    print(s, e)
