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

    elif f'.{domain}' not in valid_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    else:
        print('Email s valid')
