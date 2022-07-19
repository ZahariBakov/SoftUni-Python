from collections import defaultdict

numbers = int(input())
word_synonyms_dict = defaultdict(list)

for i in range(numbers):
    key, value = input(), input()
    word_synonyms_dict[key].append(value)

data = [f"{key} - {', '.join(value)}" for key, value in word_synonyms_dict.items()]
print("\n".join(data))
