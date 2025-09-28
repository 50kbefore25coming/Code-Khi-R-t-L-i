for _ in range(int(input())):
    s = input()
    if len(s) % 2 == 0 or s[0] == s[1]:
        print("NO")
        continue
    for i in range(2, len(s), 2):
        if s[0] != s[i]:
            print("NO")
            continue
    print("YES")