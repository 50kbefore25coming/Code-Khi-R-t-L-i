while True:
    A = list(map(int, input().split()))
    if all(x == 0 for x in A):
        break

    steps = 0
    while len(set(A)) != 1:
        B = [abs(A[i] - A[(i + 1) % 4]) for i in range(4)]
        A = B
        steps += 1

    print(steps)
