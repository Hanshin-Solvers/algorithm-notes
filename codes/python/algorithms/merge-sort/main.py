def sort_range(l, r):
    # 구간 [l, r)의 원소가 하나 이하이면 정렬 종료
    if r - l <= 1:
        return
    m = (l + r) // 2
    # 왼쪽 [l, m)과 오른쪽 [m, r)을 각각 정렬
    sort_range(l, m)
    sort_range(m, r)

    i, j, k = l, m, l
    # 두 구간의 맨 앞 값 중 작은 값을 임시 배열에 저장
    while i < m and j < r:
        # 값이 같으면 왼쪽 원소를 먼저 선택하여 기존 순서 유지
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
    # 병합한 결과를 원래 구간에 반영
    for i in range(l, r):
        lst[i] = tmp[i]


n = int(input())
lst = list(map(int, input().split()))
tmp = [0] * n
sort_range(0, n)
print(*lst)
