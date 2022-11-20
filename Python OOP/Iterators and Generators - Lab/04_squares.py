def squares(n):
    num = 1

    while num <= n:
        yield num ** 2
        num += 1


print(list(squares(5)))
print(list(squares(10)))
print(list(squares(15)))
