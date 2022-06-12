number = int(input())

percent = number // 10
points = 10 - percent

repeat_string = lambda a, b: a * b

repeat_points = repeat_string(".", points)
repeat_percent = repeat_string("%", percent)


if number < 100:
    print(f"{number}% [{repeat_percent}{repeat_points}]")
    print("Still loading...")
else:
    print("100% Complete!")
    print("[%%%%%%%%%%]")
