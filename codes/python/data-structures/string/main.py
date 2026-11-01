s = input()
l, r = map(int, input().split())

# 끝 인덱스 r은 추출 범위에서 제외됨
t = s[l - 1:r]

print(t)
