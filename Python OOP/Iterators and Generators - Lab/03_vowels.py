class vowels:
    ALL_VOWELS = "AEIUYO"

    def __init__(self, text: str):
        self.text = text
        self.vowels = [el for el in self.text if el.upper() in vowels.ALL_VOWELS]

    def __iter__(self):
        self.idx = -1
        return self

    def __next__(self):
        if self.idx == len(self.vowels) - 1:
            raise StopIteration

        self.idx += 1
        return self.vowels[self.idx]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
