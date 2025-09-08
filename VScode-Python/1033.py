<<<<<<< HEAD
import math

l, r = map(int, input().split())
for a in range(l, r - 1):
    for b in range(a + 1, r):
        if math.gcd(a, b) == 1:
            for c in range(b + 1, r + 1):
                if math.gcd(a, c) == 1 and math.gcd(b, c) == 1:
                    print(f"({a}, {b}, {c})")
=======
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

l, r = map(int, input().split())


>>>>>>> c1cc094 (8/9 2 tiếng)
