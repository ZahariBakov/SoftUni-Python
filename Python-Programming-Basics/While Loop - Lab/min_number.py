import sys

command = input()

min_number = sys.maxsize

while command != "Stop":
    if min_number > int(command):
        min_number = int(command)
    command = input()

print(min_number)
