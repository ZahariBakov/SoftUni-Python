# def squares(n):
#     num = 1
#
#     while num <= n:
#         yield num ** 2
#         num += 1


class squares:
    def __init__(self, end):
        self.start = 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration

        self.start += 1

        return self.start ** 2


print(list(squares(5)))
print(list(squares(10)))
print(list(squares(15)))
