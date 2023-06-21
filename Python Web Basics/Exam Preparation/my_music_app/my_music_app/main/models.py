from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music_app.main.validators import validate_username


class Profile(models.Model):
    MAX_LEN_NAME = 15

    username = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            MinLengthValidator(2),
            validate_username,
        )
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_LEN_ALBUM = 30

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
        max_length=MAX_LEN_ALBUM,
        unique=True,
    )

    artist = models.CharField(
        max_length=MAX_LEN_ALBUM,
        choices=CHOICES,
    )

    genre = models.CharField(
        max_length=MAX_LEN_ALBUM
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.ImageField()

    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        )
    )
