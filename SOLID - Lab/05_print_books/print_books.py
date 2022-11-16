class Book:
    def __init__(self, author: str, title: str, content: str):
        self.author = author
        self.title = title
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class PrePrintFlayer:
    def format(self, book):
        return f"-------\n{book.title}\n-------\n{book.author}\n-------"


class Printer:
    # def __init__(self, formatter):
    #     self.formatter = formatter

    def get_book(self, book: Book, formatter):
        return formatter.format(book)


normal_formatter = Formatter()
flayer_formatter = PrePrintFlayer()
b = Book("Author 1", "Title 1", "Some content")
p = Printer() #Printer(normal_formatter)
p2 = Printer() #Printer(flayer_formatter)
print(p.get_book(b, normal_formatter))
print()
print()
print(p2.get_book(b, flayer_formatter))

