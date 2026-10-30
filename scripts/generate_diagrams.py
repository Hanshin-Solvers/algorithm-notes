"""Generate individual SVG states for inline figures with live text.

Install: python -m pip install -r scripts/requirements-diagrams.txt
Run: python scripts/generate_diagrams.py
Output: src/assets/diagrams/*.svg
"""
from pathlib import Path
from html import escape
import math
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

OUT = Path(__file__).resolve().parents[1] / 'src/assets/diagrams'
FONT = TTFont(OUT.parent / 'fonts/NanumGothic-Regular.ttf')
GLYPHS, CMAP = FONT.getGlyphSet(), FONT.getBestCmap()
INK, MUTED, LINE, PAPER, ACCENT = '#242424', '#666666', '#bdbdbd', '#f5f5f5', '#505050'


class Diagram:
    def __init__(self, name, height, description, top=0):
        self.name = name
        self.description = description
        self.height = height
        self.bounds = []
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height-top}" viewBox="0 {top} 960 {height-top}" role="img" aria-labelledby="title desc">',
                      f'<title id="title">{escape(description)}</title>',
                      f'<desc id="desc">{escape(description)}</desc>',
                      f'<rect width="960" height="{height}" fill="white"/>',
                      '<g>']

    def text(self, x, y, text, size=22, color=INK, anchor='middle', bold=False):
        names = [CMAP[ord(char)] for char in str(text)]
        scale = size / FONT['head'].unitsPerEm
        width = sum(GLYPHS[name].width for name in names) * scale
        x -= width / 2 if anchor == 'middle' else width if anchor == 'end' else 0
        self.parts.append(f'<text x="{x:.2f}" y="{y+size*.35:.2f}" font-size="{size}" fill="{color}">{escape(str(text))}</text>')
        for name in names:
            bounds = BoundsPen(GLYPHS)
            GLYPHS[name].draw(bounds)
            if bounds.bounds:
                left, bottom, right, top = bounds.bounds
                baseline = y + size * .35
                self.bounds.append((x + left * scale, baseline - top * scale,
                                    x + right * scale, baseline - bottom * scale))
            x += GLYPHS[name].width * scale

    def rect(self, x, y, w, h, fill='white', stroke=LINE, radius=4):
        self.bounds.append((x-1, y-1, x+w+1, y+h+1))
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')

    def line(self, x1, y1, x2, y2, color=LINE, arrow=False, dashed=False):
        self.bounds.append((min(x1,x2)-1, min(y1,y2)-1, max(x1,x2)+1, max(y1,y2)+1))
        dash = ' stroke-dasharray="6 6"' if dashed else ''
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2"{dash}/>')
        if arrow:
            a = math.atan2(y2-y1, x2-x1)
            pts = [(x2, y2)] + [(x2-12*math.cos(a+d), y2-12*math.sin(a+d)) for d in [-.45, .45]]
            self.bounds.append((min(x for x,y in pts), min(y for x,y in pts),
                                max(x for x,y in pts), max(y for x,y in pts)))
            self.parts.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{color}"/>')

    def box(self, x, y, value, w=72, h=56, active=False, empty=False):
        self.rect(x, y, w, h, ACCENT if active else PAPER if empty else 'white', LINE)
        if value is not None:
            self.text(x+w/2, y+h/2, value, color='white' if active else INK)

    def row(self, x, y, values, w=72, active=(), indices=False):
        for i, v in enumerate(values):
            self.box(x+i*w, y, v, w=w, active=i in active, empty=v is None)
            if indices:
                self.text(x+i*w+w/2, y+78, i, size=17, color=MUTED)

    def node(self, x, y, value, active=False, r=27):
        self.bounds.append((x-r-1, y-r-1, x+r+1, y+r+1))
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{ACCENT if active else "white"}" stroke="{ACCENT if active else LINE}" stroke-width="2"/>')
        self.text(x, y, value, color='white' if active else INK)

    def edge(self, a, b, arrow=False, color=LINE, r=29):
        dx, dy = b[0]-a[0], b[1]-a[1]
        dist = math.hypot(dx, dy)
        self.line(a[0]+dx*r/dist, a[1]+dy*r/dist, b[0]-dx*r/dist, b[1]-dy*r/dist, color, arrow)

    def label(self, x, y, text):
        self.text(x, y, text, size=20, bold=True, anchor='start')

    def save(self):
        OUT.mkdir(parents=True, exist_ok=True)
        left = math.floor(min(b[0] for b in self.bounds)) - 12
        top = math.floor(min(b[1] for b in self.bounds)) - 12
        right = math.ceil(max(b[2] for b in self.bounds)) + 12
        bottom = math.ceil(max(b[3] for b in self.bounds)) + 12
        width, height = right-left, bottom-top
        self.parts[0] = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="{left} {top} {width} {height}" role="img" aria-label="{escape(self.description, quote=True)}" font-family="Nanum Gothic, sans-serif">'
        self.parts[1:3] = ['', '']
        self.parts[3] = f'<rect x="{left}" y="{top}" width="{width}" height="{height}" fill="white"/>'
        (OUT / f'{self.name}.svg').write_text('\n'.join(self.parts + ['</g></svg>'])+'\n', encoding='utf-8')


def states(name, descriptions):
    for suffix, description in zip(['before', 'after'], descriptions):
        yield Diagram(f'{name}-{suffix}', 400, description), suffix == 'after'


def indexed_row(d, values, active=()):
    d.row(0, 0, values, active=active, indices=True)


def ends(d, values, active=()):
    d.row(0, 30, values, w=90, active=active)
    d.text(45, 8, 'front', 18, MUTED)
    d.text(90*len(values)-45, 105, 'back', 18, MUTED)


def arrays():
    for d, after in states('array', ['배열 3, 1, 4, 1, 5', '세 번째 값이 9인 배열 3, 1, 9, 1, 5']):
        indexed_row(d, [3,1,9 if after else 4,1,5], (2,) if after else ())
        d.save()

    for d, after in states('array-2d', ['두 행이 1, 2, 3과 4, 5, 6인 배열', '두 번째 행의 세 번째 값이 9인 배열']):
        for j in range(3):
            d.text(40+j*80, 0, f'열 {j}', 17, MUTED)
        for i, values in enumerate([[1,2,3],[4,5,9 if after else 6]]):
            d.text(-38, 45+i*56, f'행 {i}', 17, MUTED)
            d.row(0, 17+i*56, values, w=80, active=(2,) if i and after else ())
        d.save()

    for d, after in states('dynamic-array', ['10, 20과 빈 공간 한 칸', '10, 20, 30이 저장된 배열']):
        d.row(0, 0, [10,20,30 if after else None], w=80, active=(2,) if after else ())
        d.save()

    for d, after in states('dynamic-array-2d', ['첫 행은 1, 2이고 둘째 행은 3인 배열', '첫 행은 1, 2, 9이고 둘째 행은 3인 배열']):
        d.text(-40, 28, '행 0', 18, MUTED)
        d.text(-40, 92, '행 1', 18, MUTED)
        d.row(0, 0, [1,2,9] if after else [1,2], w=80, active=(2,) if after else ())
        d.row(0, 64, [3], w=80)
        d.save()


def stack_state(d, values, active=()):
    for i, value in enumerate(values):
        d.box(0, -i*56, value, w=100, active=i in active)
    y = 28-(len(values)-1)*56
    d.text(165, y, 'top', 20, MUTED)
    d.line(140, y, 110, y, ACCENT, arrow=True)


def linear():
    for d, after in states('stack-push', ['아래에서부터 10, 20, 30, 40, 50인 스택', '아래에서부터 10, 20, 30, 40, 50, 60이고 top이 60인 스택']):
        stack_state(d, [10,20,30,40,50,60] if after else [10,20,30,40,50], (5,) if after else ())
        d.save()

    for d, after in states('stack', ['아래에서부터 10, 20, 30, 40, 50, 60인 스택', '아래에서부터 10, 20, 30, 40, 50이고 top이 50인 스택']):
        stack_state(d, [10,20,30,40,50] if after else [10,20,30,40,50,60])
        d.save()

    for d, after in states('queue-push', ['앞에서부터 10, 20, 30, 40, 50인 큐', '앞에서부터 10, 20, 30, 40, 50, 60이고 back이 60인 큐']):
        ends(d, [10,20,30,40,50,60] if after else [10,20,30,40,50], (5,) if after else ())
        d.save()

    for d, after in states('queue', ['앞에서부터 10, 20, 30, 40, 50, 60인 큐', '앞에서부터 20, 30, 40, 50, 60이고 front가 20인 큐']):
        ends(d, [20,30,40,50,60] if after else [10,20,30,40,50,60])
        d.save()

    for d, after in states('deque', ['앞에서부터 20, 30, 40, 50, 60인 덱', '앞에서부터 10, 20, 30, 40, 50, 60인 덱']):
        ends(d, [10,20,30,40,50,60] if after else [20,30,40,50,60], (0,) if after else ())
        d.save()

    for d, after in states('deque-push-back', ['앞에서부터 10, 20, 30, 40, 50, 60인 덱', '앞에서부터 10, 20, 30, 40, 50, 60, 70이고 back이 70인 덱']):
        ends(d, [10,20,30,40,50,60,70] if after else [10,20,30,40,50,60], (6,) if after else ())
        d.save()

    for d, after in states('deque-pop-front', ['앞에서부터 10, 20, 30, 40, 50, 60, 70인 덱', '앞에서부터 20, 30, 40, 50, 60, 70이고 front가 20인 덱']):
        ends(d, [20,30,40,50,60,70] if after else [10,20,30,40,50,60,70])
        d.save()

    for d, after in states('deque-pop-back', ['앞에서부터 20, 30, 40, 50, 60, 70인 덱', '앞에서부터 20, 30, 40, 50, 60이고 back이 60인 덱']):
        ends(d, [20,30,40,50,60] if after else [20,30,40,50,60,70])
        d.save()


def groups(d, sets, active=()):
    for x, values in sets:
        d.rect(x, 0, 70*len(values)+20, 80, PAPER, radius=14)
        for i, value in enumerate(values):
            d.node(x+45+i*70, 40, value, active=value in active)


def associative():
    for d, after in states('set', ['원소 1, 2, 3인 집합', '3을 삽입한 뒤에도 원소 1, 2, 3인 집합']):
        groups(d, [(0,[1,2,3])])
        d.save()

    for d, after in states('map', ['apple의 값은 1, pear의 값은 2인 맵', 'apple과 pear의 값이 모두 2인 맵']):
        d.text(70, 0, '키', 18, MUTED)
        d.text(265, 0, '값', 18, MUTED)
        for i, (key, value) in enumerate([('apple', 2 if after else 1),('pear',2)]):
            y = 20+i*65
            d.box(0, y, key, w=140, h=48)
            d.line(155, y+24, 205, y+24, arrow=True)
            d.box(220, y, value, w=90, h=48, active=after and i==0)
        d.save()


def heap_state(d, values, active=()):
    points = [(230,0),(110,86),(350,86),(30,176)]
    for i in range(1,len(values)):
        d.edge(points[(i-1)//2], points[i])
    for i, value in enumerate(values):
        d.node(*points[i], value, active=i in active)


def priorities():
    for d, after in states('heap', ['루트 1의 두 자식이 4, 5인 최소 힙', '루트 1의 자식은 2, 5이고 2의 왼쪽 자식은 4인 최소 힙']):
        heap_state(d, [1,2,5,4] if after else [1,4,5], (1,3) if after else ())
        d.save()

    for d, after in states('heap-remove', ['루트 1의 자식은 2, 5이고 2의 왼쪽 자식은 4인 최소 힙', '루트 2의 자식이 4, 5인 최소 힙']):
        heap_state(d, [2,4,5] if after else [1,2,5,4], (0,1) if after else ())
        d.save()

    for d, after in states('priority-queue', ['4, 1, 5, 2를 저장하며 다음에 꺼낼 값이 1인 우선순위 큐', '4, 5, 2를 저장하며 다음에 꺼낼 값이 2인 우선순위 큐']):
        values, chosen = ([4,5,2],2) if after else ([4,1,5,2],1)
        d.rect(0, 0, len(values)*85+20, 80, PAPER, radius=14)
        for i, value in enumerate(values):
            d.node(50+i*85, 40, value, active=value==chosen)
        d.save()


def graphs():
    d = Diagram('graph', 250, '간선 1-2, 1-3, 3-4로 연결된 무방향 그래프')
    points = {1:(0,0),2:(240,0),3:(0,100),4:(240,100)}
    for i,j in [(1,2),(1,3),(3,4)]:
        d.edge(points[i],points[j])
    for value, point in points.items():
        d.node(*point,value)
    d.save()

    d = Diagram('adjacency-list', 300, '1의 이웃은 2, 3이고 2의 이웃은 1, 3의 이웃은 1, 4, 4의 이웃은 3인 인접 리스트')
    for i, values in enumerate([[2,3],[1],[1,4],[3]]):
        d.text(-40, i*60+23, f'g[{i+1}]', 20)
        for j, value in enumerate(values):
            d.box(j*65, i*60, value, w=65, h=46)
    d.save()

    d = Diagram('tree', 300, '루트 1의 자식은 2, 3이고 정점 2의 자식은 4, 5인 트리')
    points = {1:(200,0),2:(80,93),3:(320,93),4:(0,186),5:(160,186)}
    for i,j in [(1,2),(1,3),(2,4),(2,5)]:
        d.edge(points[i],points[j])
    for value, point in points.items():
        d.node(*point,value)
    d.save()

    for d, after in states('disjoint-set', ['집합 1, 2와 집합 3과 집합 4, 5', '집합 1, 2, 3과 집합 4, 5']):
        groups(d, [(0,[1,2,3]),(280,[4,5])] if after else [(0,[1,2]),(190,[3]),(310,[4,5])])
        d.save()

    for d, after in states('segment-tree', ['배열 2, 4, 1, 5의 구간 합을 저장하고 루트 값이 12인 트리', '배열 2, 4, 3, 5의 구간 합을 저장하고 루트 값이 14인 트리']):
        values = [14,6,8,2,4,3,5] if after else [12,6,6,2,4,1,5]
        points = [(285,0),(95,81),(475,81),(0,173),(190,173),(380,173),(570,173)]
        for i in range(1,7):
            d.edge(points[(i-1)//2], points[i])
        for i, point in enumerate(points):
            d.node(*point, values[i], active=after and i in [0,2,5])
            if i>=3:
                d.text(point[0],point[1]+42,f'a[{i-3}]',17,MUTED)
        d.save()


def graph_types():
    """Static structure diagrams use the same nodes, edges and neutral palette."""
    def network(name, description, points, edges, directed=False,
                weights=None, selected=()):
        d = Diagram(name, 325, description, top=80)

        for i, (u,v) in enumerate(edges):
            d.edge(points[u], points[v], arrow=directed,
                   color=ACCENT if i in selected else LINE)
        if weights:
            for (u,v),w in zip(edges,weights):
                x=(points[u][0]+points[v][0])/2
                y=(points[u][1]+points[v][1])/2
                d.rect(x-19,y-16,38,32,stroke='white')
                d.text(x,y,w,20)
        for v,(x,y) in points.items():
            d.node(x,y,v)

        d.save()

    square={'A':(330,130),'B':(630,130),'C':(630,280),'D':(330,280)}
    chain=[('A','B'),('B','C'),('C','D')]
    network('undirected-graph',
            '화살표 없는 선은 양방향 연결을 나타냅니다.',square,chain)
    network('directed-graph',
            'A에서 B로, B에서 C로, C에서 D로 향하는 화살표.',square,chain,True)
    complete=chain+[('D','A'),('A','C'),('B','D')]
    network('complete-graph',
            '네 정점의 모든 쌍을 여섯 간선으로 연결한 구조.',square,complete)
    pentagon={str(i+1):(480+185*math.cos(-math.pi/2+i*2*math.pi/5),
                         210+100*math.sin(-math.pi/2+i*2*math.pi/5)) for i in range(5)}
    sparse=[('1','2'),('2','3'),('3','4'),('4','5')]
    dense=sparse+[('5','1'),('1','3'),('1','4'),('2','4'),('2','5')]
    network('sparse-graph',
            '다섯 정점 사이의 일부 쌍만 연결된 구조.',pentagon,sparse)
    network('dense-graph',
            '다섯 정점 사이의 많은 쌍이 연결된 구조.',pentagon,dense)
    diamond={'A':(270,205),'B':(475,130),'C':(475,280),'D':(690,205)}
    network('dag',
            'A에서 B와 C로, B와 C에서 D로 향하며 방향 사이클이 없는 구조.',
            diamond,[('A','B'),('A','C'),('B','D'),('C','D')],True)
    network('weighted-graph',
            '간선마다 가중치 1,2,3,5,6을 표시한 그래프.',
            square,chain+[('D','A'),('A','C')],weights=[1,2,3,5,6])
    mst_points = {'A':(70,170),'B':(210,40),'C':(245,285),
                  'D':(390,120),'E':(480,300),'F':(640,205)}
    mst_edges = [('A','B'),('A','C'),('B','C'),('B','D'),('C','D'),
                 ('C','E'),('D','E'),('D','F'),('E','F')]
    mst_weights = [4,3,7,2,5,8,6,9,1]
    network('mst-graph', '정점 A, B, C, D, E, F와 가중치가 있는 간선 아홉 개로 이루어진 무방향 그래프',
            mst_points, mst_edges, weights=mst_weights)
    chosen = [0,1,3,6,8]
    network('mst', '간선 AB, AC, BD, DE, EF로 여섯 정점을 연결한 최소 신장 트리. 가중치 합은 16입니다.',
            mst_points, [mst_edges[i] for i in chosen],
            weights=[mst_weights[i] for i in chosen], selected=range(5))

    d=Diagram('bst',380,'루트 8의 왼쪽에는 작은 키 3,1,6을, 오른쪽에는 큰 키 10,14를 배치한 BST.', top=80)

    points={8:(480,135),3:(330,235),10:(630,235),1:(245,335),6:(415,335),14:(715,335)}
    for u,v in [(8,3),(8,10),(3,1),(3,6),(10,14)]:
        d.edge(points[u],points[v])
    for v,p in points.items():
        d.node(*p,v,active=v==8)

    d.save()


if __name__ == '__main__':
    arrays()
    linear()
    associative()
    priorities()
    graphs()
    graph_types()
    print(f'Generated {len(list(OUT.glob("*.svg")))} diagrams in {OUT}')

