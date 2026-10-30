def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
lst = sorted(set(lst))
lo = []
hi = []

if len(lst) == 1:
    ans = lst
else:
    # 아래쪽 경계 구성
    for pt in lst:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], pt) <= 0:
            lo.pop()
        lo.append(pt)
    # 위쪽 경계 구성
    for pt in reversed(lst):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], pt) <= 0:
            hi.pop()
        hi.append(pt)
    ans = lo[:-1] + hi[:-1]

print(len(ans))
for x, y in ans:
    print(x, y)
