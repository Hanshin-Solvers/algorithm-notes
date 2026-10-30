n = int(input())
lst = list(map(int, input().split()))
k, x = map(int, input().split())

# 원소를 복사한 뒤 복사본 수정
tmp = lst.copy()
tmp[k - 1] = x

print(*lst)
print(*tmp)
