p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
dictionary = {}
for i, c in enumerate(p):
    dictionary[c] = i

while True:
    line = input()
    if line == "0":
        break
    k, s = line.split()
    k = int(k)
    encode = [p[(dictionary[c] + k) % 28] for c in s]
    print("".join(encode[::-1]))