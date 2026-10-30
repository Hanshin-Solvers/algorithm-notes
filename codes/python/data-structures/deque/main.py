from collections import deque

q = int(input())
dq = deque()

for _ in range(q):
    cmd = input().split()
    op = cmd[0]

    if op == "push_front":
        dq.appendleft(int(cmd[1]))
    elif op == "push_back":
        dq.append(int(cmd[1]))
    elif op == "size":
        print(len(dq))
    elif not dq:
        print("EMPTY")
    elif op == "front":
        print(dq[0])
    elif op == "back":
        print(dq[-1])
    elif op == "pop_front":
        print(dq.popleft())
    else:
        print(dq.pop())
