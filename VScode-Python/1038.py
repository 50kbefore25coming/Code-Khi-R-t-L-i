def dao_nguoc_so(n: int) -> int:
    sign = -1 if n < 0 else 1
    n_str = str(abs(n))[::-1]
    return sign * int(n_str)

t = int(input())
for _ in range(t):
    a = int(input())
    cnt = 0
    while a % 7 != 0:
        cnt += 1
        if cnt == 1000:
            print("-1")
            break
        a = a + dao_nguoc_so(a)
    else:
        print(a)