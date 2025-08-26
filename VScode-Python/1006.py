t = int(input())
for _ in range(t):
    a = int(input())
    ok = True
    while a:
        if a % 10 != 4 and a % 10 != 7:
            ok = False
            break
        a //= 10
    print("YES" if ok else "NO")