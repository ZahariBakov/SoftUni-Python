from collections import deque

vowels = deque(input().split())
consonants = input().split()

searched_words = ["rose", "tulip", "lotus", "daffodil"]
found = False

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for idx in range(len(searched_words)):
        if current_vowel in searched_words[idx]:
            searched_words[idx] = searched_words[idx].replace(current_vowel, '')
            if searched_words[idx] == '':
                found = True
                break

        if current_consonant in searched_words[idx]:
            searched_words[idx] = searched_words[idx].replace(current_consonant, '')
            if searched_words[idx] == '':
                found = True
                break
    if found:
        break

if found:
    if searched_words.index('') == 0:
        word = "rose"
    elif searched_words.index('') == 1:
        word = 'tulip'
    elif searched_words.index('') == 2:
        word = 'lotus'
    else:
        word = "daffodil"
    print(f"Word found: {word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
