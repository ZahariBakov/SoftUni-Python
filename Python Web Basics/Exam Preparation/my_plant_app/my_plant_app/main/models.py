from django.core.validators import MinLengthValidator
from django.db import models

from my_plant_app.main.validators import cap_first_validator, only_letter_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=(
            MinLengthValidator(2),
        ),
    )

    first_name = models.CharField(
        max_length=20,
        validators=(
            cap_first_validator,
        ),
    )

    last_name = models.CharField(
        max_length=20,
        validators=(
            cap_first_validator,
        ),
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Plant(models.Model):
    TYPES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants")
    )

    type = models.CharField(
        max_length=14,
        choices=TYPES,
    )

    name = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(2),
            only_letter_validator,
        ),
    )

    image_url = models.URLField()

    description = models.TextField()

    price = models.FloatField()
