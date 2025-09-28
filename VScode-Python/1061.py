def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    s = input()
    ok = 1
    if not snt(int(s[:3])) or not snt(int(s[-3:])):
        ok = 0
    print("YES" if ok else "NO")