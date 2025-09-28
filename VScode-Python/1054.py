for _ in range(int(input())):
    s = input()
    cnt = 1
    for i in range(0, len(s)):
        if int(s[i]) != 0:
            cnt *= int(s[i])
    print(cnt)