for _ in range(int(input())):
    s = input()
    One = 0
    Two = 1
    for i in range(len(s)):
        if i % 2 == 0:
            One += int(s[i])
        else:
            if int(s[i]) != 0:
                Two *= int(s[i])
    if Two == 1:
        Two = 0
    print(One, Two)