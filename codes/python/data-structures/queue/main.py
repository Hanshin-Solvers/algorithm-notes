from collections import deque

n = int(input())
q = deque()

for _ in range(n):
    cmd = input().split()
    op = cmd[0]

    if op == "push":
        q.append(int(cmd[1]))
    elif op == "size":
        print(len(q))
    elif not q:
        print("EMPTY")
    elif op == "front":
        print(q[0])
    else:
        print(q.popleft())
