n, k = map(int, input().split())
lst = list(map(int, input().split()))
l, r = 1, max(lst)
ans = 0

while l <= r:
    m = (l + r) // 2
    cnt = sum(x // m for x in lst)
    # 필요한 조각 수를 만들 수 있으면 답을 저장하고 더 긴 길이 탐색
    if cnt >= k:
        ans = m
        l = m + 1
    else:
        # 조각 수가 부족하면 길이를 줄여 다시 탐색
        r = m - 1

print(ans)
