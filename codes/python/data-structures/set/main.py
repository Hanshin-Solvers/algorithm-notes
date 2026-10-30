n = int(input())
# 집합에 저장하여 중복 제거
s = set(map(int, input().split()))

print(len(s))
# 집합 원소를 오름차순으로 정렬하여 출력
print(*sorted(s))
