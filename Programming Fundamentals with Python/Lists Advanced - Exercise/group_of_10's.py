numbers = list(map(int, input().split(", ")))

starting_index = 0
i = 1

while numbers:
    final_index = int(f"{i}0")
    current_list = [number for number in numbers if number in range(starting_index, final_index + 1)]
    numbers = [number for number in numbers if number not in current_list]
    print(f"Group of {final_index}'s: {current_list}")
    starting_index = final_index
    i += 1
