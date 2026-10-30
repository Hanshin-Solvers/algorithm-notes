q = int(input())
lst = []

for _ in range(q):
    cmd = input().split()
    op = cmd[0]

    if op == "append":
        lst.append(int(cmd[1]))
    elif op == "get":
        print(lst[int(cmd[1])])
    elif op == "pop":
        if lst:
            print(lst.pop())
        else:
            print("EMPTY")
    else:
        print(len(lst))
