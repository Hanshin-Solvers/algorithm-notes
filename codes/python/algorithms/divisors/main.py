n = int(input())
lst = []
i = 1

while i * i <= n:
    if n % i == 0:
        lst.append(i)
        if i != n // i:
            lst.append(n // i)
    i += 1

print(*sorted(lst))
