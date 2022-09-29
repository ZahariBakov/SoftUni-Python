text = input()

try:
    times = int(input())
    output = text * times
    print(output)
except ValueError:
    print("Variable times must be an integer")
