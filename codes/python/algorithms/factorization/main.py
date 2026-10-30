n = int(input())
lst = []
i = 2

while i * i <= n:
    while n % i == 0:
        lst.append(i)
        n //= i
    i += 1
if n > 1:
    lst.append(n)

print(*lst)
