deposit = float(input())
months = int(input())
annual_interest_rate = float(input())

annual_interest = deposit * annual_interest_rate / 100
month_interest = annual_interest / 12
total_sum = deposit + months * month_interest

print(total_sum)
