def forecast(*args):
    result = {"Sunny": [], "Cloudy": [], "Rainy": []}
    for el in args:
        location, weather = el[0], el[1]
        result[weather].append(location)

    output = ''
    for key, value in result.items():
        if value:
            sort_values = sorted(value)
            for el in sort_values:
                output += f"{el} - {key}\n"

    return output


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))

