def tower_hanoi(n, a, b, c):
    if n == 1:
        print(f"{a} -> {c}")
        return
    tower_hanoi(n - 1, a, c, b)
    print(f"{a} -> {c}")
    tower_hanoi(n - 1, b, a, c)

n = int(input())
tower_hanoi(n, 'A', 'B', 'C')