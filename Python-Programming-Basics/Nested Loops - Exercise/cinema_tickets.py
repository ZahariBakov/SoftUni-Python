movie = input()

total_ticket = 0
student_ticket = 0
standard_ticket = 0
kids_ticket = 0

while movie != "Finish":
    free_seats = int(input())
    hall_counter = 0
    current_ticket = input()
    while current_ticket != "End":
        hall_counter += 1
        total_ticket += 1
        if current_ticket == "student":
            student_ticket += 1
        elif current_ticket == "standard":
            standard_ticket += 1
        elif current_ticket == "kid":
            kids_ticket += 1
        if hall_counter >= free_seats:
            break
        current_ticket = input()
    hall_occupancy = hall_counter / free_seats * 100
    print(f"{movie} - {hall_occupancy:.2f}% full.")

    movie = input()

kids_ticket = kids_ticket / total_ticket * 100
standard_ticket = standard_ticket / total_ticket * 100
student_ticket = student_ticket / total_ticket * 100

print(f"Total tickets: {total_ticket}")
print(f"{student_ticket:.2f}% student tickets.")
print(f"{standard_ticket:.2f}% standard tickets.")
print(f"{kids_ticket:.2f}% kids tickets.")
