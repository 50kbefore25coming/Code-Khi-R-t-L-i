def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def snt(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def cong(a):
    return sum(int(d) for d in str(a))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    c = ucln(a, b)
    g = cong(c)
    if snt(g):
        print("YES")
    else:
        print("NO")
    
