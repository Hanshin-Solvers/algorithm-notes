s = input().strip()
n = int(input())
x = 0
lst = []

# 왼쪽부터 26진수의 자릿값을 누적함
for c in s:
    x = x * 26 + (ord(c) - ord('a'))
print(x)

# 낮은 자리부터 구한 뒤 순서를 뒤집음
if n == 0:
    lst.append('a')
while n > 0:
    r = n % 26
    lst.append(chr(ord('a') + r))
    n //= 26
lst.reverse()
print(''.join(lst))
