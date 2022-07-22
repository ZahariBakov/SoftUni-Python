def isdigit(text):
    return "".join([str(ch) for ch in text if ch.isdigit()])


def isletter(text):
    return "".join([ch for ch in text if ch.isalpha()])


def isother(text):
    return "".join([ch for ch in text if not ch.isalnum()])


string = input()

print(isdigit(string))
print(isletter(string))
print(isother(string))
