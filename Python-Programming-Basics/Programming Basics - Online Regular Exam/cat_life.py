import math

cat_breed = input()
cat_gender = input()

cat_life = 0
wrong_breed = False

if cat_gender == "m":
    if cat_breed == "British Shorthair":
        cat_life = (13 * 12) / 6
    elif cat_breed == "Siamese":
        cat_life = (15 * 12) / 6
    elif cat_breed == "Persian":
        cat_life = (14 * 12) / 6
    elif cat_breed == "Ragdoll":
        cat_life = (16 * 12) / 6
    elif cat_breed == "American Shorthair":
        cat_life = (12 * 12) / 6
    elif cat_breed == "Siberian":
        cat_life = (11 * 12) / 6
    else:
        wrong_breed = True
else:
    if cat_breed == "British Shorthair":
        cat_life = (14 * 12) / 6
    elif cat_breed == "Siamese":
        cat_life = (16 * 12) / 6
    elif cat_breed == "Persian":
        cat_life = (15 * 12) / 6
    elif cat_breed == "Ragdoll":
        cat_life = (17 * 12) / 6
    elif cat_breed == "American Shorthair":
        cat_life = (13 * 12) / 6
    elif cat_breed == "Siberian":
        cat_life = (12 * 12) / 6
    else:
        wrong_breed = True

if wrong_breed:
    print(f"{cat_breed} is invalid cat!")
else:
    print(f"{math.floor(cat_life)} cat months")
