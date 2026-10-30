import sys
import time

DEBUG = False
n = int(input())
lst = list(map(int, input().split()))

start = time.perf_counter()
total = 0
for x in lst:
    total += x
finish = time.perf_counter()
ms = (finish - start) * 1000

# DEBUG가 True이면 표준 오류에 기록
if DEBUG:
    print(f"sum={total}", file=sys.stderr)
    print(f"elapsed_ms={ms}", file=sys.stderr)
print(total)
