from django.core.exceptions import ValidationError


def cap_first_validator(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


def only_letter_validator(value):
    for char in value:
        if char.isspace():
            continue
        if not char.isalpha():
            raise ValidationError("Plant name should contain only letters!")

