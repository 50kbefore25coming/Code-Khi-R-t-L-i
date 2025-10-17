t = int(input())
for _ in range(t):
    a = input().strip()
    result = ""
    i = 0
    while i < len(a):
        count = 1
        while i + 1 < len(a) and a[i] == a[i + 1]:
            count += 1                             
            i += 1
        result += str(count) + a[i]
        i += 1
    print(result)