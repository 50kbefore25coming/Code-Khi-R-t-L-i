#Chỉ có các chữ số 0,2,4,6,8
#Số chữ số của khác nhau chia cho 2 dư 1

def tn(s):
    if len(s) % 2 == 1 or s != s[::-1]:
        return False
    for i in s:
        if int(i) % 2 == 1:
            return False
    return True

t = int(input())
for _ in range(t):
    a = int(input())
    for i in range(22, a, 2):
        if tn(str(i)):
            print(i, end=" ")
    print()