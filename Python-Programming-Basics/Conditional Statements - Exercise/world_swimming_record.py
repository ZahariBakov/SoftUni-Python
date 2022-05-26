old_record = float(input())
distance = float(input())
time = float(input())

delay = (distance // 15) * 12.5

new_time = time * distance + delay
if new_time < old_record:
    print(f"Yes, he succeeded! The new world record is {new_time:.2f} seconds.")
else:
    difference = new_time - old_record
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
