
t = int(input())
for _ in range(t):
    a = input().strip()
    flag = True
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            print("NO")
            flag = False
            break
    if flag:
        print("YES")