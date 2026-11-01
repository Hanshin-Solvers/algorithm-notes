n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
area = 0

for i in range(n):
    # 마지막 꼭짓점 다음은 첫 꼭짓점으로 연결
    j = (i + 1) % n
    # 인접한 두 꼭짓점의 외적을 부호 그대로 누적
    area += lst[i][0] * lst[j][1] - lst[i][1] * lst[j][0]
# 합을 구한 뒤 절댓값을 취하여 넓이의 두 배 계산
area = abs(area)

if area % 2 == 0:
    print(f"{area // 2}.0")
else:
    print(f"{area // 2}.5")
