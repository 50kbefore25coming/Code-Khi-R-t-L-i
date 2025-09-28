t = int(input())
for _ in range(t):
    s = input()
    if len(s) < 3:
        print("NO")
        continue
    ok = True
    i = 1
    while i < len(s) and s[i] > s[i - 1]:
        i += 1
    # Nếu i không chạy hoặc i chạy hết thì dừng
    if i == 1 or i == len(s):
        print("NO")
        continue
    while i < len(s) and s[i] < s[i - 1]:
        i += 1
    print("YES" if i == len(s) else "NO")