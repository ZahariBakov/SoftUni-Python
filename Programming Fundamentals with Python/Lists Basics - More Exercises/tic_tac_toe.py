first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")

first_player = 0
second_player = 0


if first_line[0] == "1":
    if first_line[1] == "1" or second_line[0] == "1" or second_line[1] == "1":
        if first_line[1] == "1":
            if first_line[2] == "1":
                print("First player won")
                exit()
        elif second_line[0] == "1":
            if third_line[0] == "1":
                print("First player won")
                exit()
        else:
            if third_line[2] == "1":
                print("First player won")
                exit()
if first_line[0] == "2":
    if first_line[1] == "2" or second_line[0] == "2" or second_line[1] == "2":
        if first_line[1] == "2":
            if first_line[2] == "2":
                print("Second player won")
                exit()
        elif second_line[0] == "2":
            if third_line[0] == "2":
                print("Second player won")
                exit()
        else:
            if third_line[2] == "2":
                print("Second player won")
                exit()
if first_line[1] == "1":
    if second_line[1] == "1":
        if third_line[1] == "1":
            print("First player won")
            exit()
if first_line[1] == "2":
    if second_line[1] == "2":
        if third_line[1] == "2":
            print("Second player won")
            exit()
if first_line[2] == "1":
    if first_line[1] == "1" or second_line[1] == "1" or second_line[2] == "1":
        if first_line[1] == "1":
            if first_line[0] == "1":
                print("First player won")
                exit()
        elif second_line[1] == "1":
            if third_line[0] == "1":
                print("First player won")
                exit()
        else:
            if third_line[0] == "1":
                print("First player won")
                exit()
if first_line[2] == "2":
    if first_line[1] == "2" or second_line[1] == "2" or second_line[2] == "2":
        if first_line[1] == "2":
            if first_line[0] == "2":
                print("Second player won")
                exit()
        elif second_line[1] == "2":
            if third_line[0] == "2":
                print("Second player won")
                exit()
        else:
            if third_line[0] == "2":
                print("Second player won")
                exit()
if second_line[0] == "1":
    if second_line[1] == "1":
        if second_line[2] == "1":
            print("First player won")
            exit()
elif second_line[0] == "2":
    if second_line[1] == "2":
        if second_line[2] == "2":
            print("Second player won")
            exit()
elif third_line[0] == "1":
    if third_line[1] == "1" or second_line[1] == "1":
        if third_line[1] == "1":
            if third_line[2] == "1":
                print("First player won")
                exit()
        else:
            if first_line[2] == "1":
                print("First player won")
                exit()
if third_line[0] == "2":
    if third_line[1] == "2" or second_line[1] == "2":
        if third_line[1] == "2":
            if third_line[2] == "2":
                print("Second player won")
                exit()
        else:
            if first_line[2] == "2":
                print("Second player won")
                exit()
else:
    print("Draw!")
