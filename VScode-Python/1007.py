import math

t = int(input())
for _ in range(t):
    a, b, c = map(float, input().split())
    years = math.ceil(math.log(c / a) / math.log(1 + b / 100))
    print(years)
