n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]

# 점수 내림차순, 번호 오름차순
lst.sort(key=lambda x: (-x[1], x[0]))
print(*[x[0] for x in lst])
