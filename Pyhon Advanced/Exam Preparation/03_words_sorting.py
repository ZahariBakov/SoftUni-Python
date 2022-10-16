def words_sorting(*args):
    result = {}
    for word in args:
        character_sum = 0
        for character in word:
            character_sum += ord(character)
        result[word] = character_sum

    dict_sum = 0
    for num in result.values():
        dict_sum += num

    if dict_sum % 2 == 0:
        sorted_result = sorted(result.items(), key=lambda x: x[0])
    else:
        sorted_result = sorted(result.items(), key=lambda x: -x[1])

    output = ''
    for el in sorted_result:
        output += f"{el[0]} - {el[1]}\n"

    return output


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
