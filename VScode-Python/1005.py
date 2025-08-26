def check(a):
    sum = 0
    while a:
        if a % 10 == 4 or a % 10 == 7:
            sum += 1
        a //= 10
    if sum == 4 or sum == 7:
        return True
    else:
        return False
    
a = int(input())
if check(a):
    print("YES")
else:
    print("NO")