def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
for ch in range(n):
    a = int(input())
    b = int(str(a)[::-1])
    print("YES" if ucln(a, b) == 1 else "NO")