def data_types(command, text):
    if command == "int":
        result = int(text) * 2
    elif command == "real":
        result = float(text) * 1.5
        result = f"{result:.2f}"
    elif command == "string":
        result = f"${text}$"
    return result


string = input()
second = input()

print(data_types(string, second))
