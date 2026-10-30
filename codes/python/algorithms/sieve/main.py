n = int(input())
prime = [True] * (n + 1)
prime[0] = prime[1] = False
i = 2

while i * i <= n:
    if prime[i]:
        for j in range(i * i, n + 1, i):
            prime[j] = False
    i += 1

print(*[i for i in range(2, n + 1) if prime[i]])
