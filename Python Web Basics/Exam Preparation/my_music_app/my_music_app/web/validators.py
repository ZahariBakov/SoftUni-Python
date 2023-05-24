from django.core import exceptions


def validate_only_alphanumeric(value):
    if not value.isalnum() and '_' not in value:
        raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")