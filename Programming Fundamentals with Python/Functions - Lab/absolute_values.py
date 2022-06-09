numbers = list(map(float, input().split(" ")))


def abs_numbers(nums):
    result = [abs(num) for num in nums]
    return result


print(abs_numbers(numbers))




