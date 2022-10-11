from simple_math_operation.helper import operation_maper

data = input().split()

first_number = float(data[0])
second_number = float(data[2])
operator = data[1]

print(f"{operation_maper[operator](first_number, second_number):.2f}")
