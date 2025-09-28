def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    s = input()
    res = 0
    ok = 1
    for i in range(0, len(s), 2):
        if int(s[i]) % 2 != 0:
            ok = 0
            break
    for i in range(1, len(s), 2):
        if int(s[i]) % 2 == 0:
            ok = 0
            break
    for i in range(0, len(s)):
        res += int(s[i])
    if not snt(res):
        ok = 0
    print("YES" if ok else "NO")