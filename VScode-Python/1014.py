a, k, n = map(int, input().split())
start = ((a // k) + 1) * k
res = []

while start <= n:
    res.append(start - a)
    start += k

if res:
    print(*res)
else:
    print(-1)

#đ hiểu công thức lấy từ đâu