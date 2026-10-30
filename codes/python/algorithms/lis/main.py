from bisect import bisect_left

n = int(input())
lst = list(map(int, input().split()))
t = []

for x in lst:
    i = bisect_left(t, x)
    if i == len(t):
        t.append(x)
    else:
        t[i] = x

print(len(t))
