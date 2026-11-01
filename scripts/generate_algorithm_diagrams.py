"""Generate algorithm figures with the shared SVG drawing primitives.

Run: python scripts/generate_algorithm_diagrams.py
Dependencies: scripts/requirements-diagrams.txt
"""
from generate_diagrams import Diagram, ACCENT, INK, LINE, MUTED, PAPER
from math import hypot


def graph(d, points, edges, selected=(), active=(), directed=False,
          weights=None, distances=None, removed=(), rejected=(), routed=None):
    for i, (u, v) in enumerate(edges):
        a, b = points[u], points[v]
        color = ACCENT if i in selected else LINE
        dx, dy = b[0] - a[0], b[1] - a[1]
        length = hypot(dx, dy)
        p = (a[0] + dx * 29 / length, a[1] + dy * 29 / length)
        q = (b[0] - dx * 29 / length, b[1] - dy * 29 / length)
        route = (routed or {}).get(i)
        if route:
            for j, (start, end) in enumerate(zip(route, route[1:])):
                d.line(*start, *end, color, directed and j == len(route) - 2)
        else:
            d.line(*p, *q, color, directed, i in removed or i in rejected)
        if i in selected:
            # A second parallel stroke makes selected edges visible in grayscale.
            ox, oy = -dy * 1.5 / length, dx * 1.5 / length
            d.line(p[0] + ox, p[1] + oy, q[0] + ox, q[1] + oy, color)
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        if route:
            mx, my = (route[1][0] + route[2][0]) / 2, route[1][1]
        if weights is not None:
            d.rect(mx - 18, my - 15, 36, 30, stroke='white')
            d.text(mx, my, weights[i], 18)
        if i in rejected:
            x, y = mx + 27, my
            d.line(x - 6, y - 6, x + 6, y + 6, INK)
            d.line(x - 6, y + 6, x + 6, y - 6, INK)
    for v, (x, y) in points.items():
        d.node(x, y, v, active=v in active)
        if distances is not None:
            d.text(x, y + 47, distances[v], 18, MUTED)


def figure(name, description):
    return Diagram('algo-' + name, 450, description)


TRAVERSAL_POINTS = {
    1: (320, 0), 2: (80, 125), 3: (320, 125), 4: (560, 125),
    5: (30, 265), 6: (230, 265), 7: (420, 265), 8: (650, 265),
    9: (120, 405), 10: (530, 405),
}
TRAVERSAL_EDGES = [
    (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7),
    (4, 8), (5, 9), (6, 9), (7, 10), (8, 10),
]


def traversal_graphs():
    from collections import deque

    p, e = TRAVERSAL_POINTS, TRAVERSAL_EDGES
    adj = {v: [] for v in p}
    for u, v in e:
        adj[u].append(v)
        adj[v].append(u)
    for neighbors in adj.values():
        neighbors.sort()

    order, path, dfs_states = [], [], []

    def visit(u):
        order.append(u)
        path.append(u)
        dfs_states.append((order[:], path[:]))
        for v in adj[u]:
            if v not in order:
                visit(v)
        path.pop()

    visit(1)
    assert order == [1, 2, 5, 9, 6, 3, 7, 10, 8, 4]

    def selected_edges(pairs):
        pairs = [set(pair) for pair in pairs]
        return [i for i, edge in enumerate(e) if set(edge) in pairs]

    for suffix, count in [('start', 4), ('deep', 6), ('return', 10)]:
        visited, stack = dfs_states[count - 1]
        d = figure('dfs-graph-' + suffix,
                   f'같은 10정점 그래프의 DFS. 방문 순서 {visited}, 현재 재귀 경로 {stack}')
        graph(d, p, e, selected_edges(zip(stack, stack[1:])), visited)
        d.text(-20, 520, '방문', 18, anchor='end')
        d.row(0, 492, visited, w=65)
        d.text(-20, 598, '경로', 18, anchor='end')
        d.row(0, 570, stack, w=65)
        d.save()

    order, dist, parent = [1], {1: 0}, {}
    q = deque([1])
    bfs_states = {}
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                parent[v] = u
                order.append(v)
                q.append(v)
        if u in [1, 4] or not q:
            bfs_states[u if q else 'done'] = (order[:], list(q), dist.copy(), parent.copy())
    assert order == list(range(1, 11))
    assert dist == {1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3}

    for suffix, state in [('start', 1), ('neighbors', 4), ('next', 'done')]:
        visited, queue, distances, parents = bfs_states[state]
        d = figure('bfs-graph-' + suffix,
                   f'같은 10정점 그래프의 BFS. 발견 순서 {visited}, 큐 {queue}. 정점 아래는 최소 거리')
        graph(d, p, e, selected_edges(parents.items()), visited)
        for v, (x, y) in p.items():
            # Keep distance labels legible where a vertical edge passes below a node.
            d.rect(x - 14, y + 34, 28, 26, stroke='white')
            d.text(x, y + 47, distances.get(v, '—'), 18, MUTED)
        d.text(-20, 520, '방문', 18, anchor='end')
        d.row(0, 492, visited, w=65)
        d.text(-20, 598, '큐', 18, anchor='end')
        if queue:
            d.row(0, 570, queue, w=65)
        else:
            d.text(0, 598, '비어 있음', 20, anchor='start')
        d.save()


def grid(d, cells, values, active=(), path=(), first_index=0):
    for c in range(len(cells[0])):
        d.text(c * 70 + 35, -25, c + first_index, 17, MUTED)
    for r, row in enumerate(cells):
        d.text(-25, r * 70 + 35, r + first_index, 17, MUTED)
        for c, cell in enumerate(row):
            d.box(c * 70, r * 70, values.get((r, c)), 70, 70,
                  active=(r, c) in active, empty=not cell)
            if not cell:
                d.line(c * 70 + 24, r * 70 + 24, c * 70 + 46, r * 70 + 46, MUTED)
                d.line(c * 70 + 24, r * 70 + 46, c * 70 + 46, r * 70 + 24, MUTED)
    for (r, c), (nr, nc) in zip(path, path[1:]):
        # Short arrows lie between numerals, without covering them.
        d.edge((c * 70 + 35, r * 70 + 35), (nc * 70 + 35, nr * 70 + 35),
               arrow=True, color=LINE, r=21)


def traversal_grids():
    cells = [[1, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 0]]
    path = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 0)]
    for suffix, count in [('start', 1), ('region', 6)]:
        d = figure('dfs-grid-' + suffix, f'DFS로 처음 {count}개 칸을 방문한 격자. 칸 안의 수는 방문 순서')
        grid(d, cells, {p: i + 1 for i, p in enumerate(path[:count])}, path[:count])
        d.save()
    cells = [[1, 0, 1], [1, 1, 1]]
    path = [(0, 0), (1, 0), (1, 1), (1, 2), (0, 2)]
    for suffix, count in [('start', 1), ('distances', 5)]:
        d = figure('bfs-grid-' + suffix, '벽을 피해 이동하는 BFS. 칸 안의 수는 시작점에서의 최소 이동 횟수')
        grid(d, cells, {p: i for i, p in enumerate(path[:count])}, path[:count], path[:count])
        d.save()


def traversal_states():
    # Each row contains states reached with the same number of BFS operations.
    p = {2: (250, 0), 3: (140, 110), 4: (360, 110),
         6: (100, 220), 5: (280, 220), 8: (460, 220),
         7: (100, 330), 9: (460, 330)}
    e = [(2, 3), (2, 4), (3, 6), (4, 5), (4, 8), (6, 7), (8, 9)]
    for suffix, active in [('first', [2, 3, 4]), ('layers', list(p))]:
        d = figure('bfs-state-' + suffix, '상태 2에서 더하기 1 또는 곱하기 2로 처음 도달한 상태와 최소 연산 횟수')
        graph(d, p, e, [i for i, edge in enumerate(e) if edge[1] in active], active, True)
        for i in range(4):
            d.text(-10, i * 110, i, 18, MUTED)
        d.save()

    p = {v: (50 + (v - 2) * 78, 50) for v in range(2, 10)}
    for suffix, path in [('deep', list(range(2, 10))), ('short', [2, 4, 8, 9])]:
        d = figure('dfs-state-' + suffix, '상태 ' + ', '.join(map(str, path)) + '을 차례로 지나는 경로')
        # Put alternative long jumps below the row to preserve arrow direction.
        for u, v in zip(path, path[1:]):
            if v == u + 1:
                d.edge(p[u], p[v], arrow=True, color=ACCENT, r=25)
            else:
                x, y = p[u][0] + 10, p[v][0] - 10
                d.line(x, 75, x, 135, ACCENT)
                d.line(x, 135, y, 135, ACCENT)
                d.line(y, 135, y, 77, ACCENT, arrow=True)
        for v, pt in p.items():
            d.node(*pt, v, active=v in path, r=24)
        d.save()


def backtracking():
    states = {'[]': (250, 25), '[1]': (250, 125),
              '[1, 2]': (80, 245), '[1, 3]': (250, 245), '[1, 4]': (420, 245)}
    e = [('[]', '[1]'), ('[1]', '[1, 2]'), ('[1]', '[1, 3]'), ('[1]', '[1, 4]')]
    for suffix, current, chosen in [('choose', '[1, 2]', [0, 1]),
                                     ('undo', '[1]', [0]),
                                     ('next', '[1, 3]', [0, 2])]:
        d = figure('backtracking-' + suffix, f'선택 목록 {current}인 백트래킹 탐색 상태')
        for i, (u, v) in enumerate(e):
            x, y = states[u]
            a, b = states[v]
            d.line(x, y + 27, a, b - 27, ACCENT if i in chosen else LINE, arrow=True)
        for value, (x, y) in states.items():
            d.box(x - 55, y - 27, value, 110, 54, active=value == current)
        d.save()
    d = figure('backtracking-prune', '세 수를 고를 때 첫 수 4를 고르면 후보 5 하나만 남는 상태')
    d.row(0, 0, [4, None, None], w=80, active=(0,))
    d.text(300, 28, '5', 22)
    d.text(300, 75, '후보', 17, MUTED)
    d.save()


def value_row(d, values, label='거리', active=(), y=430):
    d.text(0, y + 28, label, 18, anchor='end')
    for i, (key, value) in enumerate(values.items()):
        d.text(54 + i * 78, y - 20, key, 18, MUTED)
        d.box(15 + i * 78, y, '∞' if value == float('inf') else value,
              w=78, active=key in active)


def bipartite():
    from generate_diagrams import GRAPH_POINTS
    e = [(1,2),(1,3),(2,4),(3,4),(4,5),(4,6),(5,7),(6,7),(7,8)]
    for suffix, edges, rejected in [('path', e, []), ('cycle', e + [(3,6)], [9])]:
        d = figure('bipartite-' + suffix, '8개 정점의 두 그룹. 흰색은 1, 4, 7이고 진한 회색은 2, 3, 5, 6, 8입니다.')
        graph(d, GRAPH_POINTS, edges, active=[2,3,5,6,8], rejected=rejected)
        d.save()


TOPO_POINTS = {1:(30,120),2:(30,320),3:(220,35),4:(240,210),5:(400,355),
               6:(440,80),7:(590,220),8:(750,70),9:(760,325)}
TOPO_EDGES = [(1,3),(1,4),(2,4),(2,5),(3,6),(4,6),(4,7),
              (5,7),(5,9),(6,8),(7,8),(7,9)]


def topological_state(suffix, edges, processed, queue, cycle=()):
    d = figure('topological-' + suffix, f'정점 9개 중 {len(processed)}개를 처리한 위상 정렬. 남은 진입 차수와 큐를 표시합니다.')
    removed = [i for i, (u, v) in enumerate(edges) if u in processed]
    degrees = {v: '—' if v in processed else sum(b == v and a not in processed for a, b in edges)
               for v in TOPO_POINTS}
    graph(d, TOPO_POINTS, edges, selected=cycle, active=queue, directed=True, removed=removed)
    value_row(d, degrees, '진입 차수', active=queue)
    d.text(0, 550, '큐', 18, anchor='end')
    d.row(15, 522, queue + [None] * (3 - len(queue)), w=78)
    if not queue:
        d.text(310, 550, '비어 있음', 18, MUTED)
    d.save()


def topological():
    topological_state('start', TOPO_EDGES, [], [1,2])
    topological_state('one', TOPO_EDGES, [1], [2,3])
    topological_state('two', TOPO_EDGES, [1,2], [3,4,5])
    edges = TOPO_EDGES + [(8,4)]
    topological_state('cycle-start', edges, [], [1,2], [5,9,12])
    topological_state('cycle-stop', edges, [1,2,3,5], [], [5,9,12])


def shortest_paths():
    from generate_diagrams import GRAPH_POINTS, GRAPH_EDGES, GRAPH_WEIGHTS
    from heapq import heappop, heappush
    from math import inf
    p, e, w = GRAPH_POINTS, GRAPH_EDGES, GRAPH_WEIGHTS
    adj = {v: [] for v in p}
    for i, (u, v) in enumerate(e):
        adj[u].append((v, w[i], i))
    dist = {v: inf for v in p}
    dist[1] = 0
    pq, done, prev = [(0,1)], [], {}
    while pq:
        cost, u = heappop(pq)
        if u in done:
            continue
        done.append(u)
        for v, weight, i in adj[u]:
            if cost + weight < dist[v]:
                dist[v] = cost + weight
                prev[v] = i
                heappush(pq, (dist[v], v))
        suffix = {1:'direct', 3:'via', 8:'final'}.get(len(done))
        if suffix:
            d = figure('dijkstra-' + suffix, f'정점 1에서 시작한 다익스트라. 확정한 정점은 {done}이며 아래 표는 현재 거리입니다.')
            graph(d, p, e, list(prev.values()), done, True, w)
            value_row(d, dist, active=done)
            d.save()

    # Process descending source IDs so improvements need several full passes.
    w = [4,7,2,5,-3,6,2,8,4,2,5,3]
    dist = {v: inf for v in p}
    dist[1] = 0
    prev = {}
    for step in range(len(p)):
        if step:
            for i in reversed(range(len(e))):
                u, v = e[i]
                if dist[u] + w[i] < dist[v]:
                    dist[v] = dist[u] + w[i]
                    prev[v] = i
        suffix = {0:'0', 2:'1', 7:'2'}.get(step)
        if suffix:
            d = figure('bellman-' + suffix, f'전체 간선을 {step}회 확인한 벨만 포드의 거리. 간선 3에서 4의 비용은 -3입니다.')
            graph(d, p, e, list(prev.values()), directed=True, weights=w)
            value_row(d, dist)
            d.save()
    d = figure('bellman-cycle', '간선 7에서 4의 비용 -11을 추가하면 4, 6, 7의 사이클 비용은 -1입니다.')
    graph(d, p, e + [(7,4)], [7,9,12], [4,6,7], True, w + [-11])
    d.save()

    p = {1:(20,170),2:(180,30),3:(230,290),4:(400,110),5:(500,300),6:(660,165)}
    e = [(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(4,5),(4,6),(5,6),(6,2)]
    w = [3,8,2,5,1,4,2,7,1,6]
    d = figure('floyd-graph', '6개 정점과 10개 방향 간선의 가중치 그래프')
    graph(d, p, e, directed=True, weights=w,
          routed={9: [(680,145),(700,-50),(180,-50),(180,1)]})
    d.save()
    matrix = [[0 if i == j else inf for j in range(6)] for i in range(6)]
    for (u,v), weight in zip(e,w):
        matrix[u-1][v-1] = weight
    for k in range(3):
        previous = [row[:] for row in matrix]
        for i in range(6):
            for j in range(6):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        if k in [1,2]:
            suffix = 'direct' if k == 1 else 'via'
            d = figure('floyd-' + suffix, f'정점 1부터 {k+1}까지 경유를 허용한 6행 6열 거리 표. 행은 출발점, 열은 도착점입니다.')
            for i in range(6):
                d.text(i * 72 + 36, -28, i + 1, 18)
                d.text(-28, i * 56 + 28, i + 1, 18)
                values = ['∞' if n == inf else n for n in matrix[i]]
                active = [j for j in range(6) if k == 2 and matrix[i][j] < previous[i][j]]
                d.row(0, i * 56, values, w=72, active=active)
            d.save()


def kruskal():
    from generate_diagrams import GRAPH_POINTS, GRAPH_EDGES
    p, e = GRAPH_POINTS, GRAPH_EDGES
    w = [4,9,2,5,1,10,3,8,7,6,12,11]
    for suffix, selected, rejected in [('start', [], []),
                                       ('cycle', [4,2,6,0], [3]),
                                       ('tree', [4,2,6,0,9,8,11], [])]:
        d = figure('kruskal-' + suffix, '8개 정점과 12개 간선에서 진한 선으로 나타낸 크루스칼 선택 결과')
        graph(d, p, e, selected, weights=w, rejected=rejected)
        d.save()


def plane(d, xmax=4, ymin=0, ymax=4, scale=65):
    def xy(p):
        return (p[0] * scale, -p[1] * scale)
    for x in range(xmax + 1):
        d.line(x * scale, -ymax * scale, x * scale, -ymin * scale, '#e8e8e8')
        d.text(x * scale, -ymin * scale + 22, x, 16, MUTED)
    for y in range(ymin, ymax + 1):
        d.line(0, -y * scale, xmax * scale, -y * scale, '#e8e8e8')
        d.text(-25, -y * scale, y, 16, MUTED)
    d.line(-8, 0, xmax * scale + 28, 0, LINE, arrow=True)
    d.line(0, -ymin * scale + 8, 0, -ymax * scale - 28, LINE, arrow=True)
    d.text(xmax * scale + 43, 0, 'x', 17, MUTED)
    d.text(0, -ymax * scale - 43, 'y', 17, MUTED)
    return xy


def point(d, xy, value, label, offset=(13, -17)):
    x, y = xy(value)
    d.parts.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{INK}"/>')
    d.bounds.append((x - 5, y - 5, x + 5, y + 5))
    d.text(x + offset[0], y + offset[1], label, 18)


def polygon(d, points, fill):
    d.parts.append('<polygon points="' + ' '.join(f'{x},{y}' for x, y in points)
                   + f'" fill="{fill}" stroke="{ACCENT}" stroke-width="2"/>')
    d.bounds.extend((x - 1, y - 1, x + 1, y + 1) for x, y in points)


GEOMETRY_POLYGON = [(1, 3), (3, 1), (7, 2), (10, 1), (12, 5),
                    (9, 6), (11, 10), (6, 12), (5, 8), (2, 9)]
HULL_POINTS = [(1, 4), (3, 1), (7, 1), (11, 3), (12, 7), (9, 11),
               (5, 12), (1, 9), (5, 1), (1, 6), (3, 4), (5, 3),
               (7, 5), (9, 6), (6, 8), (4, 9), (8, 9), (2, 7)]


def geometry():
    def cross(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    def outline(d, xy, pts, color=LINE, arrows=False):
        for a, b in zip(pts, pts[1:] + pts[:1]):
            d.line(*xy(a), *xy(b), color, arrow=arrows)

    def polygon_points(d, xy):
        offsets = [(-17, 8), (0, 20), (0, 20), (12, 18), (15, -10),
                   (-16, -14), (16, -12), (0, -20), (-17, -10), (-17, -10)]
        for label, value, offset in zip('ABCDEFGHIJ', GEOMETRY_POLYGON, offsets):
            point(d, xy, value, label, offset)

    for suffix, ids in [('left', [0, 1, 2]), ('right', [4, 5, 6]), ('straight', [])]:
        d = figure('ccw-' + suffix, '오목한 10각형에서 세 점의 회전 방향을 비교하는 좌표 평면')
        xy = plane(d, xmax=13, ymax=13, scale=39)
        outline(d, xy, GEOMETRY_POLYGON)
        pts = [GEOMETRY_POLYGON[i] for i in ids] if ids else [(1, 3), (2, 2), (3, 1)]
        for a, b in zip(pts, pts[1:]):
            d.line(*xy(a), *xy(b), ACCENT, arrow=True)
        d.line(*xy(pts[0]), *xy(pts[2]), MUTED, dashed=True)
        polygon_points(d, xy)
        if suffix == 'straight':
            point(d, xy, (2, 2), 'K', (16, 12))
        assert cross(*pts) == {'left': 10, 'right': -14, 'straight': 0}[suffix]
        d.save()

    for suffix, pts in [
        ('cross', [(1, 2), (11, 8), (2, 10), (10, 1)]),
        ('outside', [(1, 2), (5, 4), (7, 2), (6, 8)]),
        ('overlap', [(1, 2), (7, 6), (4, 4), (10, 8)]),
    ]:
        d = figure('intersection-' + suffix, '비스듬한 두 선분 AB와 CD의 교차, 연장선 교차, 겹침 비교')
        xy = plane(d, xmax=12, ymax=11, scale=42)
        a, b, c, e = pts
        d.line(*xy(a), *xy(b), ACCENT)
        d.line(*xy(c), *xy(e), ACCENT)
        if suffix == 'outside':
            d.line(*xy(b), *xy((8, 5.5)), MUTED, dashed=True)
        if suffix == 'overlap':
            x1, y1 = xy(c)
            x2, y2 = xy(b)
            d.line(x1, y1 - 3, x2, y2 - 3, ACCENT)
            d.line(x1, y1 + 3, x2, y2 + 3, ACCENT)
        for label, value in zip('ABCD', pts):
            point(d, xy, value, label)
        d.save()

    pts = GEOMETRY_POLYGON
    terms = [a[0] * b[1] - a[1] * b[0] for a, b in zip(pts, pts[1:] + pts[:1])]
    assert sum(terms) == 153 and terms[7] == -12
    for suffix in ['boundary', 'triangles']:
        d = figure('area-' + suffix, '오목한 10각형 ABCDEFGHIJ와 원점에서 만든 부호 있는 삼각형')
        xy = plane(d, xmax=13, ymax=13, scale=39)
        polygon(d, [xy(v) for v in pts], PAPER)
        if suffix == 'triangles':
            polygon(d, [xy(v) for v in [(0, 0), pts[7], pts[8]]], '#d5d5d5')
            for value in pts:
                d.line(*xy((0, 0)), *xy(value), LINE, dashed=True)
            outline(d, xy, pts, ACCENT)
            for a, b in [((0, 0), pts[7]), (pts[7], pts[8]), (pts[8], (0, 0))]:
                d.line(*xy(a), *xy(b), ACCENT, arrow=True)
            point(d, xy, (0, 0), 'O', (-16, -18))
        polygon_points(d, xy)
        d.save()

    def chain(values):
        result = []
        states = []
        for value in values:
            before = result[:]
            removed = []
            while len(result) >= 2 and cross(result[-2], result[-1], value) <= 0:
                removed.append(result.pop())
            result.append(value)
            states.append((value, before, result[:], removed))
        return result, states

    lower, states = chain(sorted(HULL_POINTS))
    upper, _ = chain(sorted(HULL_POINTS, reverse=True))
    hull = lower[:-1] + upper[:-1]
    assert hull == HULL_POINTS[:8]
    for suffix in ['points', 'boundary']:
        d = figure('hull-' + suffix, '외곽 8점, 변 위 2점, 내부 8점으로 이루어진 18점 집합')
        xy = plane(d, xmax=13, ymax=13, scale=39)
        if suffix == 'boundary':
            polygon(d, [xy(v) for v in hull], PAPER)
        for value in HULL_POINTS:
            point(d, xy, value, '')
        d.save()

    value, before, after, removed = next(state for state in states if state[0] == (7, 1))
    assert removed == [(6, 8), (5, 1)]
    labels = {(1, 4): 'A', (3, 1): 'B', (5, 1): 'C', (6, 8): 'D', (7, 1): 'E'}
    for suffix, path in [('before', before + [value]), ('after', after)]:
        d = figure('hull-turn-' + suffix, '18점 집합에서 새 점 E를 처리하며 시계 방향의 D와 일직선의 C를 제거')
        xy = plane(d, xmax=13, ymax=13, scale=39)
        for a, b in zip(path, path[1:]):
            d.line(*xy(a), *xy(b), ACCENT, arrow=True)
        for v in HULL_POINTS:
            point(d, xy, v, labels.get(v, ''), (0, 20) if v[1] == 1 else (13, -17))
        d.save()


def area_term_figures():
    o, a, b, q = (0, 0), (4, 0), (1, 3), (5, 3)
    for suffix in ['positive', 'negative']:
        d = figure('area-term-' + suffix, '외적의 절댓값 12는 평행사변형 넓이이며 삼각형 넓이 6의 두 배')
        xy = plane(d, xmax=5, ymax=3, scale=72)
        polygon(d, [xy(p) for p in [o, a, q, b]], 'white')
        polygon(d, [xy(p) for p in [o, a, b]], '#dddddd')
        d.line(*xy(b), *xy((1, 0)), MUTED, dashed=True)
        order = [o, a, b, o] if suffix == 'positive' else [o, b, a, o]
        for u, v in zip(order, order[1:]):
            d.line(*xy(u), *xy(v), ACCENT, arrow=True)
        d.text(*xy((1.7, 1)), '6', 24)
        d.text(*xy((3.3, 2)), '6', 24, MUTED)
        for label, p, offset in [('O', o, (-16, -18)), ('A', a, (15, -17)),
                                  ('B', b, (-15, -18)), ('Q', q, (15, -17))]:
            point(d, xy, p, label, offset)
        d.save()


def grid_dp_figures():
    cells = [[1, 1, 1, 1, 1], [1, 1, 0, 1, 1],
             [1, 0, 1, 1, 1], [1, 1, 1, 1, 1]]
    dp = [[0] * 5 for _ in range(4)]
    dp[0][0] = 1
    for r in range(4):
        for c in range(5):
            if not cells[r][c] or (r, c) == (0, 0):
                continue
            dp[r][c] = (dp[r - 1][c] if r else 0) + (dp[r][c - 1] if c else 0)
    assert dp == [[1, 1, 1, 1, 1], [1, 2, 0, 1, 2], [1, 0, 0, 1, 3], [1, 1, 1, 2, 5]]
    for suffix in ['start', 'before', 'after']:
        d = figure('grid-dp-' + suffix, '오른쪽과 아래쪽 이동의 경로 수. X는 벽이며 빈칸은 계산 전 상태')
        if suffix == 'start':
            values, active = {(0, 0): 1}, [(0, 0)]
        else:
            values = {(r, c): dp[r][c] for r in range(4) for c in range(5) if cells[r][c]}
            active = [(2, 4), (3, 3)]
            if suffix == 'before':
                del values[3, 4]
            else:
                active += [(3, 4)]
        grid(d, cells, values, active=active, first_index=1)
        if suffix != 'start':
            for r, c in [(2, 4), (3, 3)]:
                d.edge((c * 70 + 35, r * 70 + 35), (4 * 70 + 35, 3 * 70 + 35),
                       arrow=True, color=LINE, r=21)
        d.save()


if __name__ == '__main__':
    traversal_graphs()
    traversal_grids()
    traversal_states()
    backtracking()
    bipartite()
    topological()
    shortest_paths()
    kruskal()
    geometry()
    area_term_figures()
    grid_dp_figures()
    print('Generated 55 algorithm SVG figures.')
