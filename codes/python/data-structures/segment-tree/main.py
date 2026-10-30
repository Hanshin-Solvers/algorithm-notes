N = 10000  # 최대 원소 수
t = [0] * (N * 4)


# 노드 k의 담당 구간 [s, e)에서 인덱스 i의 값을 x로 갱신
def update(k, s, e, i, x):
    if e - s == 1:
        t[k] = x
        return

    m = (s + e) // 2
    if i < m:
        update(k * 2, s, m, i, x)
    else:
        update(k * 2 + 1, m, e, i, x)

    t[k] = t[k * 2] + t[k * 2 + 1]


# [l, r) 구간 합 질의
def query(k, s, e, l, r):
    if r <= s or e <= l:
        return 0
    if l <= s and e <= r:
        return t[k]

    m = (s + e) // 2
    return query(k * 2, s, m, l, r) + query(k * 2 + 1, m, e, l, r)


n, q = map(int, input().split())
lst = list(map(int, input().split()))

# 루트 1에서 [0, n) 구간을 기준으로 입력값 저장
for i, x in enumerate(lst):
    update(1, 0, n, i, x)

for _ in range(q):
    cmd = input().split()
    op = cmd[0]

    if op == "set":
        i = int(cmd[1])
        x = int(cmd[2])

        update(1, 0, n, i, x)
    else:
        l = int(cmd[1])
        r = int(cmd[2])

        print(query(1, 0, n, l, r))
