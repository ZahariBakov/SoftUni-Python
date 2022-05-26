beginning_of_range = input()
end_of_range = input()
valid_barcode = " "

for first_number in range(int(beginning_of_range[0]), int(end_of_range[0]) + 1):
    for second_number in range(int(beginning_of_range[1]), int(end_of_range[1]) + 1):
        for third_number in range(int(beginning_of_range[2]), int(end_of_range[2]) + 1):
            for fourth_number in range(int(beginning_of_range[3]), int(end_of_range[3]) + 1):
                if first_number % 2 != 0:
                    if second_number % 2 != 0:
                        if third_number % 2 != 0:
                            if fourth_number % 2 != 0:
                                valid_barcode += f"{first_number}{second_number}{third_number}{fourth_number}"
                                print(valid_barcode, end=" ")
                                valid_barcode = ""
