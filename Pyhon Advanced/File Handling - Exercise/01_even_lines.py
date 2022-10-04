file_path = './text.txt'
symbols = ["-", ",", ".", "!", "?"]

with open(file_path) as file:
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for el in symbols:
                result = result.replace(el, "@")

            print(result)
