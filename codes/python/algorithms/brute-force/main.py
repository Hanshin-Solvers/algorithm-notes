def search(d, s):
    if d == 2:
        return 1 if s == target else 0

    cnt = 0
    for x in range(1, n + 1):
        cnt += search(d + 1, s + x)
    return cnt


n, target = map(int, input().split())
print(search(0, 0))
