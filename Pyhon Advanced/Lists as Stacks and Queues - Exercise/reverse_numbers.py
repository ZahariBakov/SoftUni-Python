original_number = input()

stack = original_number.split(" ")
reversed_number = ""

while stack:
    reversed_number += stack.pop() + " "

print(reversed_number)
