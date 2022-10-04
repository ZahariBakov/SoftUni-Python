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

with open(file_path) as file:
    idx = 1
    for line in file:
        count_letter, count_symbols = letters_symbols_count(line)
        print(f"Line {idx}: {line.strip()} ({count_letter})({count_symbols})")
        idx += 1
