def so(s):
    ok = True
    if s != s[::-1]:
        ok = False
    for i in range(0, len(s)):
        if int(s[i]) % 2 != 0:
            ok = False
    if len(s) % 2 != 0:
        ok = False
    return ok

t = int(input())
for _ in range(t):
    s = int(input())
    for i in range(22, s):
        if so(str(i)):
            print(i, end=" ")
    print("") 