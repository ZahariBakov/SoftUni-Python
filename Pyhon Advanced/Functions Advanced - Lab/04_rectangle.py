def rectangle(*args):
    def area(length, width):
        area_result = length * width

        return area_result

    def perimeter(length, width):
        perimeter_result = 2 * (length + width)

        return perimeter_result

    for el in args:
        if type(el) != int:
            return "Enter valid values!"

    return f"Rectangle area: {area(args[0], args[1])}" + "\n" \
           + f"Rectangle perimeter: {perimeter(args[0], args[1])}"


print(rectangle(2, 10))
print(rectangle('2', 10))
