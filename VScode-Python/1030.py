def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
count = 0
# nếu b = 2 thì start = 10 và end = 100 "**" là luy thừa
start = 10**(b - 1)
end = 10**(b)
for i in range(start, end):
    if ucln(i, a) == 1:
        count += 1
        print(i, end=" ")
        if count == 10:
            count = 0
            print()