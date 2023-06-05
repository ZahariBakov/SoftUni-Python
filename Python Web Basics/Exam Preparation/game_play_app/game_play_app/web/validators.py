from django.core.exceptions import ValidationError


def valid_rating_validator(value):
    if not 0.1 <= value <= 5.0:
        raise ValidationError(Exception)
