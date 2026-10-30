import sys

it = iter(map(int, sys.stdin.buffer.read().split()))
n = next(it)
ans = []

for _ in range(n):
    x = next(it)
    ans.append(str(x * 2))

sys.stdout.write("\n".join(ans) + "\n")
