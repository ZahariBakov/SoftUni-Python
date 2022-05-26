length = int(input())
width = int(input())
height = int(input())
percent = float(input())

aquarium_volume = length * width * height
volume_in_liter = aquarium_volume * 0.001
occupied_space = percent / 100

total_liter = volume_in_liter * (1 - occupied_space)

print(total_liter)
