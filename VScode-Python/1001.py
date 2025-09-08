import math

def ktra(a):
    if a % 2 == 0:
        return True
    else:
        return False

n = int(input())
if ktra(n):
    print("CHAN")
else:
    print("LE")