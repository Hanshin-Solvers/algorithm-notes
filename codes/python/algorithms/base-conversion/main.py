b, c = map(int, input().split())
s = input().strip()
digit = "0123456789ABCDEF"
x = 0
out = []

for ch in s:
    x = x * b + digit.index(ch)

if x == 0:
    out.append("0")
while x > 0:
    out.append(digit[x % c])
    x //= c

print("".join(reversed(out)))
