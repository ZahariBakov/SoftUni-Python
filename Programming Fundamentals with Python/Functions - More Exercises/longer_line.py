import math


def cartesian_points(x, y):
    return x ** 2 + y ** 2


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

length_first = cartesian_points(x1, y1)
length_second = cartesian_points(x2, y2)
length_third = cartesian_points(x3, y3)
length_fourth = cartesian_points(x4, y4)

if length_first + length_second > length_third + length_fourth:
    x1 = math.floor(x1)
    y1 = math.floor(y1)
    x2 = math.floor(x2)
    y2 = math.floor(y2)
    if length_first > length_second:
        print(f"({x2}, {y2})({x1}, {y1})")
    else:
        print(f"({x1}, {y1})({x2}, {y2})")
else:
    x3 = math.floor(x3)
    y3 = math.floor(y3)
    x4 = math.floor(x4)
    y4 = math.floor(y4)
    if length_third > length_fourth:
        print(f"({x4}, {y4})({x3}, {y3})")
    else:
        print(f"({x3}, {y3})({x4}, {y4})")
