# 세 점의 외적으로 기준 직선에 대한 방향 계산
def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def overlap(a, b, c, d):
    return max(min(a, b), min(c, d)) <= min(max(a, b), max(c, d))


a1, a2, b1, b2 = map(int, input().split())
c1, c2, d1, d2 = map(int, input().split())
a, b = (a1, a2), (b1, b2)
c, d = (c1, c2), (d1, d2)
# 외적을 -1, 0, 1로 바꾸어 양쪽 선분의 방향 조건 비교
x = sign(cross(a, b, c))
y = sign(cross(a, b, d))
z = sign(cross(c, d, a))
w = sign(cross(c, d, b))

# 네 점이 일직선이면 x좌표와 y좌표의 공통 구간 확인
if x == 0 and y == 0 and z == 0 and w == 0:
    ok = overlap(a1, b1, c1, d1) and overlap(a2, b2, c2, d2)
else:
    # 각 직선의 양쪽에 상대 선분의 끝점이 놓이는지 확인
    ok = x * y <= 0 and z * w <= 0

print("YES" if ok else "NO")
