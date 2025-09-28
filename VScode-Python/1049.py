def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    s = input()
    if not is_prime(len(s)):
        print("NO")
        continue
    cnt_snt = 0
    cnt = 0
    for i in range(0, len(s)):
        x = int(s[i])
        if is_prime(x):
            cnt_snt += 1
        else:
            cnt += 1
    print("YES" if cnt_snt > cnt else "NO")