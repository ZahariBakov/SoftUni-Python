number = input()

prime_num = 0
non_prime_num = 0

while number != "stop":
    current_number = int(number)
    if current_number < 0:
        print("Number is negative.")
        number = input()
        continue
    prime = True
    for i in range(2, current_number):
        if current_number % i == 0:
            non_prime_num += current_number
            prime = False
            break
    if prime:
        prime_num += current_number

    number = input()

print(f"Sum of all prime numbers is: {prime_num}")
print(f"Sum of all non prime numbers is: {non_prime_num}")
