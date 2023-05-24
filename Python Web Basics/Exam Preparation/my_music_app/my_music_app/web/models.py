from django.core import exceptions
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validate_only_alphanumeric(value):
    if not value.isalnum() and '_' not in value:
        raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    NAME_MAX_LENGTH = 15
    NAME_MIN_LENGTH = 2

    username = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            validate_only_alphanumeric,
        ),
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    ALBUM_MAX_LEN = 30

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER_MUSIC = "Other"

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    album_name = models.CharField(
        max_length=ALBUM_MAX_LEN,
        unique=True,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        max_length=ALBUM_MAX_LEN,
    )

    genre = models.CharField(
        max_length=ALBUM_MAX_LEN,
        choices=MUSICS,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.URLField(
        verbose_name='Image URL',
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        )
    )
