def upper_part(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(col, end=' ')
        print()


def bottom_part(n):
    for row in range(n - 1, 0, -1):
        for col in range(1, row + 1):
            print(col, end=' ')
        print()