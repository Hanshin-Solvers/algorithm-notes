from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
c = [-1] * (n + 1)
q = deque()
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ok = True
for i in range(1, n + 1):
    # 아직 방문하지 않은 연결 요소마다 새 탐색 시작
    if c[i] != -1:
        continue
    c[i] = 0
    q.append(i)
    while q:
        u = q.popleft()
        for v in g[u]:
            if c[v] == -1:
                # 인접한 정점에 반대 색 배정
                c[v] = 1 - c[u]
                q.append(v)
            # 간선 양 끝의 색이 같으면 이분 그래프 조건 위반
            elif c[v] == c[u]:
                ok = False

print("YES" if ok else "NO")
