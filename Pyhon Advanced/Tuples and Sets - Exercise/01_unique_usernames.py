n = int(input())

unique = set()

for _ in range(n):
    name = input()

    unique.add(name)

print("\n".join(unique))
