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
    for i in range(0, len(s)):
        res += int(s[i])
    print("YES" if snt(res) else "NO")
