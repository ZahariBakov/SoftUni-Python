import math


def cartesian_points(x1, y1, x2, y2):
    abs1 = 1 ** 2 + y1 ** 2
    abs2 = x2 ** 2 + y2 ** 2
    if abs1 > abs2:
        return (x2, y2)
    else:
        return (x1, y1)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x1 = math.floor(x1)
y1 = math.floor(y1)
x2 = math.floor(x2)
y2 = math.floor(y2)

print(cartesian_points(x1, y1, x2, y2))
