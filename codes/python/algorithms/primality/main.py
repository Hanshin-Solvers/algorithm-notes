n = int(input())
ok = n >= 2
i = 2

while i * i <= n:
    if n % i == 0:
        ok = False
    i += 1

print("YES" if ok else "NO")
