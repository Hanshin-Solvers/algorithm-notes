import heapq

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
d = [0] * (n + 1)
heap = []
ans = []
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    # d[v]: 아직 처리하지 않은 진입 간선의 수
    d[b] += 1
for i in range(1, n + 1):
    # 선행 조건이 없는 정점을 넣고 작은 번호부터 선택
    if d[i] == 0:
        heapq.heappush(heap, i)

while heap:
    u = heapq.heappop(heap)
    ans.append(u)
    for v in g[u]:
        # 현재 정점에서 나가는 간선을 제거하여 다음 정점의 진입 차수 감소
        d[v] -= 1
        if d[v] == 0:
            heapq.heappush(heap, v)

# 모든 정점을 처리하지 못했으면 방향 사이클 존재
if len(ans) != n:
    print("IMPOSSIBLE")
else:
    print(*ans)
