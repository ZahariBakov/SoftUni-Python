from fibonacci_sequence.create_sequence import create_sequence
from fibonacci_sequence.locate_number import locate_num

command = input()
sequence = []

while command != "Stop":
    name = command.split()[0]
    number = int(command.split()[-1])
    if name == "Create":
        sequence = create_sequence(number)
        print(*sequence)
    elif name == "Locate":
        locate_num(number, sequence)

    command = input()
