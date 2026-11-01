"""Validate built links, formula output, scope, and displayed code originals."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import json
from catalog import entries

ROOT = Path(__file__).resolve().parents[1]
BASE = '/algorithm-notes/'


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.panels, self.codes, self.tabs = set(), [], {}, {}, {}
        self.current_panel = None
        self.in_code = False
        self.math_count = 0
        self.math_errors = 0
        self.next_link = None
        self.images = []
        self.diagrams = []
        self.captions = []
        self.caption = None
        self.headings = []
        self.heading = None
        self.example_io = False
        self.related_links = []
        self.related_started = False
        self.feed(source)

    def handle_starttag(self, tag, pairs):
        a = dict(pairs)
        if 'related-algorithms' in a.get('class', '').split(): self.related_started = True
        if 'data-related-algorithm' in a:
            self.related_links.append((a['data-related-algorithm'], a['href']))
        if 'data-code-panel' in a:
            assert not self.related_started, 'Related algorithms must follow the example code.'
        if tag == 'figcaption': self.caption = ''
        if tag in ['h2','h3']:
            self.heading = ''
        if 'example-io' in a.get('class','').split(): self.example_io = True
        if tag == 'img':
            self.images.append(a)
        if tag == 'svg' and 'note-diagram' in a.get('class', '').split():
            self.diagrams.append(a)
        if 'id' in a:
            assert a['id'] not in self.ids, f"Duplicate id: {a['id']}"
            self.ids.add(a['id'])
        for key in ('href','src'):
            if key in a: self.links.append(a[key])
        if 'katex' in a.get('class','').split(): self.math_count += 1
        if 'katex-error' in a.get('class','').split(): self.math_errors += 1
        if a.get('role') == 'tab': self.tabs[a['data-language']] = a['aria-selected']
        if 'data-code-panel' in a:
            self.current_panel = a['data-code-panel']
            self.panels[self.current_panel] = 'hidden' in a
            self.codes[self.current_panel] = ''
        if tag == 'code' and self.current_panel: self.in_code = True
        if 'next-page' in a.get('class','').split(): self.next_link = a['href']

    def handle_endtag(self, tag):
        if tag == 'figcaption' and self.caption is not None:
            self.captions.append(self.caption.strip())
            self.caption = None
        if tag in ['h2','h3'] and self.heading is not None:
            self.headings.append(self.heading.strip())
            self.heading = None
        if tag == 'code': self.in_code = False

    def handle_data(self, data):
        if self.caption is not None: self.caption += data
        if self.heading is not None: self.heading += data
        if self.in_code: self.codes[self.current_panel] += data


def main():
    pages = {path: Page(path.read_text(encoding='utf-8')) for path in (ROOT/'dist').rglob('*.html')}
    assert pages, 'Build the site first.'
    for path, page in pages.items():
        assert page.math_errors == 0, path
        for link in page.links:
            parsed = urlparse(link)
            if parsed.scheme or parsed.netloc: continue
            if not parsed.path:
                target = path
            else:
                assert parsed.path.startswith(BASE), f'{path}: base path missing: {link}'
                target = ROOT/'dist'/unquote(parsed.path[len(BASE):])
                if target.is_dir() or parsed.path.endswith('/'): target /= 'index.html'
            assert target.is_file(), f'{path}: missing {target}'
            if parsed.fragment and target in pages:
                assert unquote(parsed.fragment) in pages[target].ids, f'{path}: missing anchor {link}'
    topics = entries()
    config = json.loads((ROOT/'src/data/example-languages.json').read_text(encoding='utf-8'))
    related = json.loads((ROOT/'src/data/related-algorithms.json').read_text(encoding='utf-8'))
    all_topics = {topic for _, topic in topics}
    for topic, targets in related.items():
        assert topic in all_topics, f'Unknown related-link source: {topic}'
        assert targets and len(targets) == len(set(targets)), f'{topic}: empty or duplicate related links'
        assert topic not in targets and set(targets) <= all_topics, f'{topic}: invalid related topic'
    graph_order = ['dijkstra', 'bellman-ford', 'floyd-warshall', 'kruskal', 'topological-sort', 'bipartite']
    assert [topic for _, topic in topics if topic in graph_order] == graph_order, 'Graph algorithm order'
    code_count = 0
    for index, (category, topic) in enumerate(topics):
        enabled = config.get(topic, ['cpp', 'java', 'python'])
        code_count += len(enabled)
        page = pages[ROOT/'dist/notes'/category/topic/'index.html']
        neighbors = set(related.get(topic, [])) | {source for source, targets in related.items() if topic in targets}
        expected_related = [(target, BASE + f'notes/{target_category}/{target}/')
                            for target_category, target in topics if target in neighbors]
        assert page.related_links == expected_related, f'{topic}: related algorithm links'
        for target, link in page.related_links:
            target_page = pages[ROOT/'dist'/link[len(BASE):]/'index.html']
            assert (topic, BASE + f'notes/{category}/{topic}/') in target_page.related_links, f'{topic} → {target}: missing reverse link'
        if expected_related:
            assert page.headings[-1] == '연관 문서', f'{topic}: related section must be last'
        else:
            assert not page.related_started, f'{topic}: empty related section'
        expected_images = 8 if topic == 'deque' else 6 if topic == 'priority-queue' else 4 if topic in ['array', 'dynamic-array', 'stack', 'queue'] else 3 if topic == 'graph-density' else 1 if topic in ['tree', 'bst', 'dag', 'weighted-graph'] else 2
        if category == 'algorithms':
            expected_images = {
                'dfs-graph': 3, 'dfs-grid': 2, 'dfs-state': 2,
                'bfs-graph': 3, 'bfs-grid': 2, 'bfs-state': 2,
                'backtracking': 4, 'bipartite': 2, 'topological-sort': 5,
                'dijkstra': 3, 'bellman-ford': 4, 'floyd-warshall': 3,
                'kruskal': 3, 'ccw': 3, 'segment-intersection': 3,
                'polygon-area': 4, 'convex-hull': 4, 'grid-dp': 3,
            }.get(topic, 0)
        elif category != 'data-structures':
            expected_images = 0
        assert not page.images, f'{topic}: expected inline SVG instead of image element'
        assert len(page.diagrams) == expected_images, f'{topic}: missing inline diagram'
        assert len(page.captions) == expected_images, f'{topic}: missing figure caption'
        for number, caption in enumerate(page.captions, 1):
            prefix = f'▲ [그림 {number}] '
            assert caption.startswith(prefix) and caption[len(prefix):].strip(), f'{topic}: figure caption order or text'
        for img in page.diagrams:
            assert img.get('aria-label', '').strip(), f'{topic}: missing diagram description'
            assert int(img.get('width', 0)) > 0 and int(img.get('height', 0)) > 0, f'{topic}: missing diagram dimensions'
        assert page.math_count > 0, f'{topic}: expected rendered formulas'
        assert page.tabs == {lang: 'true' if lang == 'cpp' else 'false' for lang in enabled}
        assert page.panels == {lang: lang != 'cpp' for lang in enabled}
        if not enabled:
            assert not page.example_io, f'{topic}: conceptual page has sample I/O'
            assert not any('예제' in heading for heading in page.headings), f'{topic}: conceptual page has example section'
        else:
            example_headings = ['예제', '문제', '입력', '출력', '예제 입력', '예제 출력', '예제 코드']
            if expected_related: example_headings.append('연관 문서')
            start = page.headings.index('예제')
            assert page.headings[start:] == example_headings, f'{topic}: problem section order'
            assert page.example_io, f'{topic}: missing sample I/O'
        if topic == 'segment-tree':
            assert enabled == ['cpp','java','python'] and page.example_io
        if topic == 'priority-queue':
            assert all(heading in page.headings for heading in ['힙의 구조', '힙에 원소 삽입', '힙에서 최솟값 제거'])
        if topic == 'graph-direction':
            assert page.headings.index('무방향 그래프') < page.headings.index('방향 그래프')
        for language, filename in [('cpp','main.cpp'),('java','Main.java'),('python','main.py')]:
            if language not in enabled:
                continue
            original = (ROOT/'codes'/language/category/topic/filename).read_text(encoding='utf-8')
            assert page.codes[language].rstrip() == original.rstrip(), f'{topic}/{language}: displayed source mismatch'
        expected = BASE+'notes/'+topics[index+1][0]+'/'+topics[index+1][1]+'/' if index+1 < len(topics) else None
        assert page.next_link == expected, f'{topic}: next-page order'
    for category in ['algorithms', 'utilities']:
        page = pages[ROOT/'dist'/category/'index.html']
        expected_links = {BASE + f'notes/{category}/{topic}/' for c, topic in topics if c == category}
        assert expected_links <= set(page.links), f'{category}: missing topic links'
    assert len(pages) == len(topics) + 3, 'Expected notes, overview, algorithms, and utilities pages.'
    print(f'PASS: {len(pages)} pages; {sum(len(p.diagrams) for p in pages.values())} inline SVGs and captions; links, math, language defaults, {code_count} code sources, next-page order, category scope.')


if __name__ == '__main__': main()
