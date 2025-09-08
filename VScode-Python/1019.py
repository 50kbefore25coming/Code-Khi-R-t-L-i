n = int(input())
for _ in range(n):
    s1 = str(input())
    s2 = s1[::-1]
    flag = True
    for i in range(1, len(s1)):
        a = abs(ord(s1[i]) - ord(s1[i - 1]))
        b = abs(ord(s2[i]) - ord(s2[i - 1]))
        if a != b:
            flag = False
            break
    print("YES" if flag else "NO")