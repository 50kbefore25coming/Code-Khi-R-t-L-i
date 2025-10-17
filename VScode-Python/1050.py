result = []
chars = ["A", "B", "C"]

def backtrack(chars, n, cur):
    if len(cur) >= 3:
        s = "".join(cur)
        if all(ch in s for ch in chars):
            if s.count("A") <= s.count("B") <= s.count("C"):
                result.append(s)
    if len(cur) == n:
        return
    for ch in chars:
        cur.append(ch)
        backtrack(chars, n, cur)
        cur.pop()

n = int(input())
backtrack(chars, n, [])
print("\n".join(sorted(result, key=lambda x: (len(x), x))))