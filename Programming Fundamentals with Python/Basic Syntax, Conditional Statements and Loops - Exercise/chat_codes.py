lines = int(input())

for i in range(lines):
    command = int(input())
    if command == 88:
        print("Hello")
    elif command == 86:
        print("How are you?")
    elif command != 86 and command < 88:
        print("GREAT!")
    else:
        print("Bye.")
