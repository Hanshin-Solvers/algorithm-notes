import math

a, b, c, n = map(int, input().split())

x = (a + b + c) / 3
up = math.ceil(x)
down = math.floor(x)
near = round(x)

# 소수점 아래 n자리를 고정하고 부족한 자리는 0으로 채움
print(f"{x:.{n}f}")
print(up, down, near)
