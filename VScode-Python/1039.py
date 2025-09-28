t = int(input())
for _ in range(t):
    s = input()
    ok = True
    for i in range(1, len(s), 2):
        if s[i] != s[1]:
            ok = False
    for i in range(0, len(s), 2):
        if s[i] != s[0]:
            ok = False
    print("YES" if ok else "NO")

