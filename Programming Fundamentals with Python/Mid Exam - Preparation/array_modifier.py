numbers = list(map(int, input().split()))

command = input()

while command != "end":
    if "swap" in command:
        first_element = int(command.split()[1])
        second_element = int(command.split()[2])
        numbers[first_element], numbers[second_element] = numbers[second_element], numbers[first_element]

    elif "multiply" in command:
        index = int(command.split()[1])
        multiplier = int(command.split()[2])
        numbers[index] *= numbers[multiplier]

    elif "decrease" in command:
        for num in range((len(numbers))):
            numbers[num] -= 1

    command = input()


print(", ".join(str(x) for x in numbers))
