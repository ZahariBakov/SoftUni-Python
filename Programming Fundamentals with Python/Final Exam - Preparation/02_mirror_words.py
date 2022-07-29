import re

pattern = r'@([A-Za-z]{3,})@@([A-Za-z]{3,})@|#([A-Za-z]{3,})##([A-Za-z]{3,})#'
text = input()

matches = re.findall(pattern, text)

if matches:
    print(f"{len(matches)} word pairs found!")

else:
    print("No word pairs found!")

word_one = []
word_two = []

for match in matches:
    current_word_one = ''
    current_word_two = ''
    for word in match:
        if len(word) > 2:
            if len(current_word_two) < len(current_word_one):
                current_word_two = word

                if current_word_one == current_word_two[::-1]:
                    word_one.append(current_word_one)
                    word_two.append(current_word_two)

            else:
                current_word_one = word

if not word_two:
    print("No mirror words!")

else:
    words = []
    print("The mirror words are:")
    for index in range(len(word_one)):
        words.append(f"{word_one[index]} <=> {word_two[index]}")
    print(', '.join(words))
