numbers = list(map(float, input().split(" ")))


def rounding(nums):
    result = [round(num) for num in nums]
    return result


print(rounding(numbers))
