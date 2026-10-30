n, m = map(int, input().split())
r, c = map(int, input().split())
r -= 1
c -= 1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 0

for k in range(4):
    nr = r + dr[k]
    nc = c + dc[k]
    if nr < 0 or nr >= n or nc < 0 or nc >= m:
        continue
    # 출력 번호는 1부터 시작
    print(nr + 1, nc + 1)
    cnt += 1

if cnt == 0:
    print("NONE")
