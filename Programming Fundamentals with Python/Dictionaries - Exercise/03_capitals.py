countries = input().split(", ")
cities = input().split(", ")

dictionary = dict(zip(countries, cities))

data = [f"{key} -> {value}" for key, value in dictionary.items()]
print("\n".join(data))
