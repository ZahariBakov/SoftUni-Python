projection_tipe = input()
rows = int(input())
columns = int(input())

total_places = rows * columns
ticket_price = 0

if projection_tipe == "Premiere":
    ticket_price = 12
elif projection_tipe == "Normal":
    ticket_price = 7.5
elif projection_tipe == "Discount":
    ticket_price = 5

income = total_places * ticket_price

print(f"{income:.2f} leva")
