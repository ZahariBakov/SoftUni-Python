from django.core.exceptions import ValidationError


def validate_first_char_in_name(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def validate_only_letter(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Fruit name should contain only letters!")
