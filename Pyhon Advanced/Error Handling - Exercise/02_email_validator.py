class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    email = input()

    valid_domains = ['.com', '.bg', '.org', '.net']
    email = email.split('@')

    if len(email) != 2:
        raise MustContainAtSymbolError('Email must contain @"')

    name = email[0]
    domain = email[1].split('.')[1]

    if 4 >= len(name):
        raise NameTooShortError('Name must be more than 4 characters')

    if f'.{domain}' not in valid_domains:
        raise InvalidDomainError(f'Domain must be one of the following: {" ".join(valid_domains)}')

    print('Email s valid')
