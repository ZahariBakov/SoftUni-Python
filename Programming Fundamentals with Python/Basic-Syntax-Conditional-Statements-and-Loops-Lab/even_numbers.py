lines = int(input())

for _ in range(lines):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f"{current_number} is odd!")
        break

else:
    print("All numbers are even.")
