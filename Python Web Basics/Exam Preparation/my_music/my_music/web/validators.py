from django.core.exceptions import ValidationError


def validate_username(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
