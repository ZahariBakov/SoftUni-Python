from string import punctuation


def letters_symbols_count(text):
    letters = 0
    symbols = 0

    for el in text:
        if el.isalpha():
            letters += 1
        elif el in punctuation:
            symbols += 1

    return letters, symbols


input_file_path = './text.txt'
output_file_path = './output.txt'

with open(input_file_path, 'r') as input_file, \
        open(output_file_path, 'w') as output_file:
    idx = 1
    for line in input_file:
        count_letter, count_symbols = letters_symbols_count(line)
        output_file.write(f"Line {idx}: {line.strip()} "
                          f"({count_letter})({count_symbols})\n")
        idx += 1
