# Decision with numbers:
#
# numbers = list(map(int, input().split(", ")))
#
#
# def palindrome(number):
#     for num in range(len(numbers)):
#         current_number = numbers[num]
#         palindrome = False
#         temporary_number = current_number
#         reversed_number = 0
#         while current_number > 0:
#             digit = current_number % 10
#             reversed_number = reversed_number * 10 + digit
#             current_number = current_number // 10
#         if temporary_number == reversed_number:
#             palindrome = True
#
#         print(palindrome)
#
#
# palindrome(numbers)

# Decision with string:
#
string = input().split(", ")


def is_palindrome(number):
    result = ""
    for i in range(len(number) - 1, -1, -1):
        result += number[i]
    return result == number


for number in string:
    print(is_palindrome(number))