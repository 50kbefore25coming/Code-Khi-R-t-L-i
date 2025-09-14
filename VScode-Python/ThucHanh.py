MAX = 10**7
Mang = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    for j in range(i, MAX + 1, i):
        Mang[j] += 1

print(Mang[50])