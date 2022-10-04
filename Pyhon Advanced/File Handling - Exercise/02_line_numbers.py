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


file_path = './text.txt'

with open(file_path) as input_file, \
        open('./output.txt', 'w') as output_file:
    idx = 1
    for line in input_file:
        count_letter, count_symbols = letters_symbols_count(line)
        output_file.write(f"Line {idx}: {line.strip()} "
                          f"({count_letter})({count_symbols})\n")
        idx += 1
