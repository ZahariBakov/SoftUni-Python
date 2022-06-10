number = int(input())


def perfect_numbers(a):
    sum = 0

    for num in range(1, a):
        if a % num == 0:
            sum += num

    if sum == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_numbers(number)
