def so(s):
    ok = True
    if len(s) % 2 != 0 or s != s[::-1]:
        ok = False
    for i in s:
        if int(i) % 2 != 0:
            ok = False
    return ok

for t in range(int(input())):
    s = int(input())
    for i in range(22, s, 2):
        if so(str(i)):
            print(i, end=" ")
    print("")