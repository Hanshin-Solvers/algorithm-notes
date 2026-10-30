def sort_range(l, r):
    if r - l <= 1:
        return
    m = (l + r) // 2
    sort_range(l, m)
    sort_range(m, r)

    i, j, k = l, m, l
    while i < m and j < r:
        if lst[i] <= lst[j]:
            tmp[k] = lst[i]
            i += 1
        else:
            tmp[k] = lst[j]
            j += 1
        k += 1
    while i < m:
        tmp[k] = lst[i]
        i += 1
        k += 1
    while j < r:
        tmp[k] = lst[j]
        j += 1
        k += 1
    for i in range(l, r):
        lst[i] = tmp[i]


n = int(input())
lst = list(map(int, input().split()))
tmp = [0] * n
sort_range(0, n)
print(*lst)
