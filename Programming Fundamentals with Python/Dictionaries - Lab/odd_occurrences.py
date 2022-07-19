from collections import defaultdict

words = input().split(" ")
dictionary = defaultdict(int)

for word in words:
    dictionary[word.lower()] += 1

print(" ".join([word for word, count in dictionary.items() if count % 2 != 0]))
