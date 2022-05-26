orders = int(input())

total_price = 0

for current_order in range(orders):
    capsule_price = float(input())
    days = int(input())
    capsule_needed = int(input())
    if capsule_price < 0.01 or capsule_price > 100.00:
        continue
    if days < 1 or days > 31:
        continue
    if capsule_needed < 1 or capsule_needed > 2000:
        continue
    current_price = capsule_price * days * capsule_needed
    total_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")

print(f"Total: ${total_price:.2f}")
