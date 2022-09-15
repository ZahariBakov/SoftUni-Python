n = int(input())
guestс_list = set()

for _ in range(n):
    guest = input()
    guestс_list.add(guest)

guest_coming = input()

while guest_coming != "END":
    guestс_list.discard(guest_coming)
    guest_coming = input()

print(len(guestс_list))
print("\n".join(sorted(guestс_list)))
