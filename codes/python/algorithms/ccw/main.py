def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))

v = cross(a, b, c)
if v > 0:
    print(1)
elif v == 0:
    print(0)
else:
    print(-1)
