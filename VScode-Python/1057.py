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
    for i in range(len(s)):
        digit = int(s[i])
        if snt(i):
            if not snt(digit):
                ok = 0
                break
        else:
            if snt(digit):
                ok = 0
                break
    print("YES" if ok else "NO")