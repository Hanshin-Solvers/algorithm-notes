from collections import deque

a, b = map(int, input().split())
d = [-1] * 101
q = deque([a])

d[a] = 0
while q:
    x = q.popleft()
    for y in [x + 1, x * 2]:
        if y > 100 or d[y] != -1:
            continue
        # 처음 도달한 횟수가 최소 연산 횟수임
        d[y] = d[x] + 1
        q.append(y)

print(d[b])
