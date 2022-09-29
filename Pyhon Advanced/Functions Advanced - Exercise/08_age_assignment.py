def age_assignment(*args, **kwargs):
    result = []
    for key, value in kwargs.items():
        for el in args:
            if el.startswith(key):
                text = f"{el} is {value} years old."
                result.append(text)
    result = sorted(result)

    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
