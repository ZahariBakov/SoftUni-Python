def repeat_text(data):
    repeated_text = "".join(text * len(text) for text in data)
    print(repeated_text)


repeat_text(input().split(" "))
