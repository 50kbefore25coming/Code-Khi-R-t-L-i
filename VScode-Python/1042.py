t = int(input())
for _ in range(t):
    s = input()
    i = 0
    ok = True
    while i < len(s):
        if s[i] not in "012":
            ok = False
            break
        i += 1
    print("YES" if ok else "NO") 