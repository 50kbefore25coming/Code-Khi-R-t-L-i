t = int(input())
for _ in range(t):
    a = str(input().strip())
    flag = True
    tong = sum(int(i) for i in a)
    if tong % 10 != 0:
        flag = False
    else:
        for i in range(len(a) - 1):
            if abs(int(a[i]) - int(a[i + 1])) != 2:
                flag = False
                break
    print("YES" if flag else "NO")