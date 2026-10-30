a, b = map(int, input().split())

q = a // b
r = a % b
up = q
if r > 0:
    up += 1

print(q, up, r)
