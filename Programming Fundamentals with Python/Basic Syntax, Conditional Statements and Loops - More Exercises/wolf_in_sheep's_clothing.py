animals = input().split(", ")

animals_reversed = animals[::-1]

for i in range(len(animals_reversed)):
    if animals_reversed[0] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif animals_reversed[i] != "sheep":
        print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")
