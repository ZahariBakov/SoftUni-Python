countries = input().split(", ")
cities = input().split(", ")

dictionary = dict(zip(countries, cities))

for key, value in dictionary.items():
    print(f"{key} -> {value}")
