number_of_pours = int(input())

capacity = 255
tank = 0

for i in range(number_of_pours):
    current_pour = int(input())
    if tank + current_pour > capacity:
        print("Insufficient capacity!")
        continue
    else:
        tank += current_pour

print(tank)
