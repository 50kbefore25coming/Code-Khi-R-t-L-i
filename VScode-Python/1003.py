n = int(input())
for _ in range(n):
    a = int(input())
    b = 10
    while a > b:
        a = ((a + b // 2) // b) * b
        b *= 10
    print(a)