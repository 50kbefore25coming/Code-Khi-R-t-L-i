t = int(input())
for _ in range(t):
    a = input().strip()
    i = 0
    result = ""
    while i < len(a):           # lặp đến hết chuỗi a
        char = a[i]             # lấy kí tự tại vị trí i
        count = int(a[i + 1])   # lấy kí tự bên cạnh char chuyển thành số nguyên
        result += char * count  # nhân kí tự vd: 'A' * 3 = 'AAA'
        i += 2
    print(result)