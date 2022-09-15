n = int(input())
guests_list = set()

for _ in range(n):
    guest = input()
    guests_list.add(guest)

guest_coming = input()

while guest_coming != "END":
    guests_list.discard(guest_coming)
    guest_coming = input()

print(len(guests_list))
print("\n".join(sorted(guests_list)))
