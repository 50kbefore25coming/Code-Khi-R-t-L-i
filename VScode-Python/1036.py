t = int(input())
for _ in range(t):
    a = float(input())
    s = 0.0
    if a % 2 == 0:
        i = 2
        while i <= a:
            s += 1 / i
            i += 2
    else:
        i = 1
        while i <= a:
            s += 1 / i
            i += 2
    print(f"{s:.6f}")