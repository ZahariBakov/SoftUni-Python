from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.web.validators import validate_first_char_in_name, validate_only_letter


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=(
            MinLengthValidator(2),
            validate_first_char_in_name,
        ),
    )

    last_name = models.CharField(
        max_length=35,
        validators=(
            MinLengthValidator(1),
            validate_first_char_in_name,
        ),
    )

    email = models.EmailField(
        max_length=40,
    )

    password = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(8),
        ),
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    age = models.IntegerField(
        blank=True,
        null=True,
        default=18,
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            validate_only_letter,
        ),
    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
