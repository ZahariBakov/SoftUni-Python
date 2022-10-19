from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(y) for y in input().split()])

presents = {
            "Diamond Jewellery": 0,
            "Gemstone": 0,
            "Gold": 0,
            "Porcelain Sculpture": 0
            }

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    present_point = current_magic + current_material

    if present_point < 100:
        if present_point % 2 == 0:
            current_material *= 2
            current_magic *= 3
            present_point = current_magic + current_material
        else:
            present_point *= 2

    if present_point > 499:
        present_point /= 2

    if 99 < present_point < 200:
        presents["Gemstone"] += 1
    elif 199 < present_point < 300:
        presents["Porcelain Sculpture"] += 1
    elif 299 < present_point < 400:
        presents["Gold"] += 1
    elif 399 < present_point < 500:
        presents["Diamond Jewellery"] += 1

if (presents["Gemstone"] > 0 and presents["Porcelain Sculpture"] > 0) \
        or (presents["Gold"] > 0 and presents["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(y) for y in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key, value in presents.items():
    if value > 0:
        print(f"{key}: {value}")
