import sys

for line in sys.stdin:
    # 빈 줄 건너뛰기
    if not line.strip():
        continue
    a, b = map(int, line.split())
    print(a + b)
