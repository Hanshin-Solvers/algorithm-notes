from bisect import bisect_left

n = int(input())
lst = list(map(int, input().split()))
# t[k]: 길이 k+1 수열의 최소 끝값, pos[k]: 해당 원소 위치, p[i]: 이전 원소 위치
t = []
pos = []
p = [-1] * n
ans = []

for i, x in enumerate(lst):
    # 현재 값 이상인 첫 위치를 찾아 같은 값으로 수열 길이가 늘어나는 것을 방지함
    k = bisect_left(t, x)

    # 후보 교체 전에 이전 원소의 위치 저장
    if k > 0:
        p[i] = pos[k - 1]
    if k == len(t):
        t.append(x)
        pos.append(i)
    else:
        t[k] = x
        pos[k] = i

# 가장 긴 수열의 끝에서 이전 위치를 따라 복원
i = pos[-1]
while i != -1:
    ans.append(lst[i])
    i = p[i]
ans.reverse()

print(len(ans))
print(*ans)
