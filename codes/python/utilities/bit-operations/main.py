x, k = map(int, input().split())
mask = 1 << k

bit = (x >> k) & 1
on = x | mask
off = x & ~mask
flip = x ^ mask

print(bit, on, off, flip)
