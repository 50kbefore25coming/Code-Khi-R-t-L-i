import math

n = int(input())
for _ in range(n):
    a = int(input())
    b = ["1"]
    # isqrt trả về số nguyên sqrt trả về float số thực
    for i in range(2, math.isqrt(a) + 1):
        count = 0
        while a % i == 0:
            a //= i
            count += 1
        if count > 0:
            b.append(f"{i}^{count}")
    if a > 1:
        b.append(f"{a}^1")
    print(" * ".join(b))
