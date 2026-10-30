"""Convert the bundled Nanum Gothic originals to self-hosted WOFF2 fonts.

Install: python -m pip install -r scripts/requirements-diagrams.txt
Run: python scripts/prepare_fonts.py
"""
from pathlib import Path
from fontTools.ttLib import TTFont

fonts = Path(__file__).resolve().parents[1] / 'src/assets/fonts'
for path in sorted(fonts.glob('*.ttf')):
    with TTFont(path) as font:
        font.flavor = 'woff2'
        font.save(path.with_suffix('.woff2'))
