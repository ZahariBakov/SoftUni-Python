n = int(input())
guests = set()

for _ in range(n):
    guest = input()
    guests.add(guest)

guest_coming = input()

while guest_coming != "END":
    guests.discard(guest_coming)
    guest_coming = input()

print(len(guests))
print("\n".join(sorted(guests)))
