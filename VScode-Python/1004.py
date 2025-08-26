import math

def snt(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    k = sum(1 for i in range(1, n) if math.gcd(i, n) == 1)
    if  snt(k):
        print("YES")
    else:
        print("NO")
