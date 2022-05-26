import math

video_card_price = int(input())
adapter_price = int(input())
electricity_per_day = float(input())
profit_video_card_per_day = float(input())

total_price_video_cards = 13 * video_card_price
total_price_adapters = 13 * adapter_price
total_spent_money = total_price_adapters + total_price_video_cards + 1000
profit_video_card_per_day = profit_video_card_per_day - electricity_per_day
profit_per_day = 13 * profit_video_card_per_day
return_money = math.ceil(total_spent_money / profit_per_day)

print(total_spent_money)
print(return_money)
