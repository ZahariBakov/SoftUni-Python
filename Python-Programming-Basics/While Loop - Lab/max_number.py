import sys

command = input()

max_num = -sys.maxsize

while command != "Stop":
    if max_num < int(command):
        max_num = int(command)
    command = input()
print(max_num)
