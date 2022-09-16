n = int(input())
unique = set()

for _ in range(n):
    elements = input().split()

    for chemical_compound in elements:
        unique.add(chemical_compound)

print("\n".join(unique))
