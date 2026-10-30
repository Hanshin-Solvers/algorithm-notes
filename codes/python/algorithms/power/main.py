def power(a, b):
    if b == 0:
        return 1
    x = power(a, b // 2)
    x *= x
    if b % 2 == 1:
        x *= a
    return x


a, b = map(int, input().split())
print(power(a, b))
