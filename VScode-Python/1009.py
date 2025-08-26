a = str(input())

cnt_upper = sum(1 for ch in a if ch.isupper())
cnt_lower = sum(1 for ch in a if ch.islower())

if cnt_upper <= cnt_lower:
    print(a.lower())
else:
    print(a.upper())