t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    if n <= 10:
        print(n)
    else:
        place = 10
        while n > place:
            n = ((n + place // 2) // place) * place
            place *= 10
        print(n)