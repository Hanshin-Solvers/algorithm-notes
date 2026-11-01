def mul(a, b):
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # a의 i행과 b의 j열에서 같은 위치의 곱을 누적
                c[i][j] += a[i][k] * b[k][j]
    return c


def power(a, b):
    # 행렬의 0제곱은 대각 원소가 1인 항등행렬
    if b == 0:
        t = [[0] * n for _ in range(n)]
        for i in range(n):
            t[i][i] = 1
        return t
    # 절반 지수의 결과를 한 번 계산하여 재사용
    t = power(a, b // 2)
    t = mul(t, t)
    # 홀수 지수에서 제곱 후 남은 행렬 a를 한 번 곱함
    if b % 2 == 1:
        t = mul(t, a)
    return t


n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# 절반 지수의 결과를 한 번 계산하여 재사용
t = power(a, b)

for row in t:
    print(*row)
