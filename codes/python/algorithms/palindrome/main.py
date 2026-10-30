s = input()
l = 0
r = len(s) - 1
ok = True

while l < r:
    if s[l] != s[r]:
        ok = False
        break
    l += 1
    r -= 1

print("YES" if ok else "NO")
