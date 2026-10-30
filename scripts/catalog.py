"""Read the navigation shared by site and code verification."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def entries():
    result = []
    for category, filename in [('data-structures', 'navigation.json'), ('algorithms', 'navigation-algorithms.json'), ('utilities', 'navigation-utilities.json')]:
        groups = json.loads((ROOT / 'src/data' / filename).read_text(encoding='utf-8'))
        for group in groups:
            for item in group.get('items', [group]):
                result.append((category, item['id']))
    assert len({topic for _, topic in result}) == len(result), 'Topic IDs must be unique.'
    return result


def case_path(category, topic):
    folder = ROOT / 'tests/cases'
    if category != 'data-structures':
        folder /= category
    return folder / f'{topic}.json'
