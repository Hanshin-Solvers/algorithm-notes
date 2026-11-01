# 최대 100개 단어 × 길이 20 + 루트
t = [[0] * 26 for _ in range(2001)]
fin = [False] * 2001
sz = 0


def add(s):
    global sz
    u = 0

    for c in s:
        x = ord(c) - ord('a')
        if t[u][x] == 0:
            # 해당 문자로 이어지는 노드가 없으면 새 노드 생성
            sz += 1
            t[u][x] = sz
        u = t[u][x]
    # 접두사 경로와 완성된 단어를 구분하는 끝 표시
    fin[u] = True


def find(s):
    u = 0

    for c in s:
        x = ord(c) - ord('a')
        if t[u][x] == 0:
            # 해당 접두사 경로가 없으므로 검색 종료
            return -1
        u = t[u][x]
    return u


n, q = map(int, input().split())
for _ in range(n):
    s = input()
    add(s)

for _ in range(q):
    op, s = input().split()
    u = find(s)

    # 단어 검색은 끝 표시까지 확인
    if op == 'word':
        ok = u != -1 and fin[u]
    else:
        ok = u != -1

    if ok:
        print('YES')
    else:
        print('NO')
