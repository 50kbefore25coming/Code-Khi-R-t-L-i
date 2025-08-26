
t = int(input())
for _ in range(t):
    a = int(input())
    s = str(a)
    dau = s[0 : 2]
    cuoi = s[-2 :]
    print("YES" if int(dau) == int(cuoi) else "NO")