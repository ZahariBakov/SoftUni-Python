from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from my_music.web.validators import validate_username


class Profile(models.Model):
    MAX_LEN_NAME = 30
    MIN_LEN_NAME = 2

    username = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_NAME),
            validate_username,
        ),
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )


class Album(models.Model):
    MAX_LEN_NAME = 30

    CHOICES = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    )

    album_name = models.CharField(
        max_length=MAX_LEN_NAME,
        unique=True,
    )

    artist = models.CharField(
        max_length=MAX_LEN_NAME
    )

    genre = models.CharField(
        max_length=MAX_LEN_NAME,
        choices=CHOICES,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.IntegerField()

    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        ),
    )
