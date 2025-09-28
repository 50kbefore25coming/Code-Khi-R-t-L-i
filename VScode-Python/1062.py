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
    if not snt(len(s)):
        ok = 0
    one = 0
    two = 0
    for i in range(len(s)):
        if snt(int(s[i])):
            one += 1
        else:
            two += 1
    if two > one:
        ok = 0
    print("YES" if ok else "NO")