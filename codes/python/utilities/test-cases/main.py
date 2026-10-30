t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    # 케이스마다 합 초기화
    total = 0
    for x in lst:
        total += x
    print(total)
