def tribonacci_lenght(number):
    tribonacci_sequence = [1]
    for _ in range(1, number):
        new_number = sum(tribonacci_sequence[:-4:-1])
        tribonacci_sequence.append(new_number)
    tribonacci_string_sequence = [str(x) for x in tribonacci_sequence]
    return " ".join(tribonacci_string_sequence)


length = int(input())

print(tribonacci_lenght(length))
