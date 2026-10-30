def search(start):
    if len(lst) == r:
        print(*lst)
        return

    # 남은 수로 필요한 자리를 채울 수 있을 때만 선택
    for x in range(start, n - (r - len(lst)) + 2):
        lst.append(x)
        search(x + 1)
        lst.pop()  # 선택 복구


n, r = map(int, input().split())
lst = []
search(1)
