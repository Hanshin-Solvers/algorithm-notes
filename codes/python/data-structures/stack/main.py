q = int(input())
st = []

for _ in range(q):
    cmd = input().split()
    op = cmd[0]

    if op == "push":
        st.append(int(cmd[1]))
    elif op == "size":
        print(len(st))
    elif not st:
        print("EMPTY")
    elif op == "top":
        print(st[-1])
    else:
        print(st.pop())
