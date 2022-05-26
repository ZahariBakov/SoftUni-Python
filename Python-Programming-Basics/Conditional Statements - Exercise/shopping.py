budget = float(input())
numbers_video_card = int(input())
numbers_processors = int(input())
numbers_ram = int(input())

video_card_price = 250 * numbers_video_card
processor_price = video_card_price * 0.35 * numbers_processors
ram_price = video_card_price * 0.1 * numbers_ram
total_price = video_card_price + processor_price + ram_price

if numbers_processors < numbers_video_card:
    total_price -= total_price * 0.15
difference = abs(budget - total_price)
if total_price > budget:
    print(f"Not enough money! You need {difference:.2f} leva more!")
else:
    print(f"You have {difference:.2f} leva left!")
