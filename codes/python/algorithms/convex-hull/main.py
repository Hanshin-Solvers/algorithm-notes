# 세 점의 방향 판별: 양수는 반시계, 0은 일직선, 음수는 시계 방향
def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
# x좌표 우선, 같으면 y좌표 순으로 정렬하여 경계 탐색 순서 결정
lst = sorted(set(lst))
lo = []
hi = []

if len(lst) == 1:
    ans = lst
else:
    # 아래쪽 경계 구성
    for pt in lst:
        # 시계 방향 또는 일직선인 마지막 점을 제거하여 반시계 방향 유지
        while len(lo) >= 2 and cross(lo[-2], lo[-1], pt) <= 0:
            lo.pop()
        lo.append(pt)
    # 위쪽 경계 구성
    for pt in reversed(lst):
        # 시계 방향 또는 일직선인 마지막 점을 제거하여 반시계 방향 유지
        while len(hi) >= 2 and cross(hi[-2], hi[-1], pt) <= 0:
            hi.pop()
        hi.append(pt)
    # 위아래 경계에 중복되는 양 끝점 제외
    ans = lo[:-1] + hi[:-1]

print(len(ans))
for x, y in ans:
    print(x, y)
