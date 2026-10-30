n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
area = 0

for i in range(n):
    j = (i + 1) % n
    area += lst[i][0] * lst[j][1] - lst[i][1] * lst[j][0]
area = abs(area)

if area % 2 == 0:
    print(f"{area // 2}.0")
else:
    print(f"{area // 2}.5")
