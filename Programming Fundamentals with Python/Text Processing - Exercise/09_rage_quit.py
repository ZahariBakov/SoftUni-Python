string = input().upper()

current_char = ''
current_num = ''
new_messages = ''

for char in string:
    if char.isdigit():
        current_num += char
    else:
        if current_num != '':
            new_messages += current_char * int(current_num)
            current_char = char
            current_num = ''
        else:
            current_char += char

if current_num != '':
    new_messages += current_char * int(current_num)

unique_symbol = set(new_messages)
print(f"Unique symbols used: {len(unique_symbol)}")

print(new_messages)
