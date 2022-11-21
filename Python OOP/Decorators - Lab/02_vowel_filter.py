from functools import wraps


def vowel_filter(function):

    @wraps(function)
    def wrapper():
        result = function()
        vowels = "aoueiy"

        return [x for x in result if x.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
