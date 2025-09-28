for _ in range(int(input())):
    s = input()
    res = 0
    for i in range(0, len(s)):
        res += int(s[i])
    if res <= 10:
        print("NO")
        continue
    print("YES" if str(res) == ''.join(reversed(str(res))) else "NO")
