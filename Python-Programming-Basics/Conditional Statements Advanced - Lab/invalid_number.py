number = int(input())

range = 100 <= number <= 200
zero = number == 0
valid = range or zero

if not valid:
    print("invalid")

