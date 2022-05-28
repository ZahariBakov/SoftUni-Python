number = int(input())

prime = True

if number > 1:
    for num in range(2, number):
        if number % num == 0:
            prime = False
            break

print(prime)
