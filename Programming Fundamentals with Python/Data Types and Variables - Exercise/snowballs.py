snowball_number = int(input())

snowball_weight = 0
snowball_time = 0
snowball_quality = 0
snowball_value = 0

for i in range(snowball_number):
    current_snowball_weight = int(input())
    current_snowball_time = int(input())
    current_snowball_quality = int(input())
    current_snowball_value = pow((current_snowball_weight / current_snowball_time), current_snowball_quality)
    if current_snowball_value > snowball_value:
        snowball_weight = current_snowball_weight
        snowball_time = current_snowball_time
        snowball_quality = current_snowball_quality
        snowball_value = int(current_snowball_value)

print(f"{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})")
