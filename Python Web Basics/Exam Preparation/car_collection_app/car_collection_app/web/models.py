from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from car_collection_app.web.validators import valid_year_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=(
            MinLengthValidator(2, "The username must be a minimum of 2 chars"),
        ),
    )

    email = models.EmailField()

    age = models.IntegerField(
        validators=(
            MinValueValidator(18),
        ),
    )

    password = models.CharField(
        max_length=30,
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username


class Car(models.Model):
    TYPES = (
        ("Sport Car", "Sport Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other")
    )

    type = models.CharField(
        max_length=10,
        choices=TYPES,
    )

    model = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(2),
        ),
    )

    year = models.IntegerField(
        validators=(
            valid_year_validator,
        ),
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(1),
        ),
    )

    def __str__(self):
        return self.model
