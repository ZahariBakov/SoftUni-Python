length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
total_liters = volume * 0.001
percents = percent * 0.01
water_liters = total_liters * (1-percents)

print("%.3f" % water_liters)
