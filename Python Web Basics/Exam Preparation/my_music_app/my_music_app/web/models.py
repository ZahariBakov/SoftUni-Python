from enum import Enum

from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music_app.web.validators import validate_only_alphanumeric


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


# With enums:

class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class AlbumGenres(ChoicesEnum):
    POP = 'Pop Music'
    JAZZ = "Jazz Music"
    RNB = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIP_HOP = "Hip Hop Music"
    OTHER = "Other"


class Album(models.Model):
    ALBUM_MAX_LEN = 30

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
        choices=AlbumGenres.choices(),
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


# Without enums:
#
# class Album(models.Model):
#     ALBUM_MAX_LEN = 30
#
#     POP_MUSIC = 'Pop Music'
#     JAZZ_MUSIC = "Jazz Music"
#     RNB_MUSIC = "R&B Music"
#     ROCK_MUSIC = "Rock Music"
#     COUNTRY_MUSIC = "Country Music"
#     DANCE_MUSIC = "Dance Music"
#     HIP_HOP_MUSIC = "Hip Hop Music"
#     OTHER_MUSIC = "Other"
#
#     MUSICS = (
#         (POP_MUSIC, POP_MUSIC),
#         (JAZZ_MUSIC, JAZZ_MUSIC),
#         (RNB_MUSIC, RNB_MUSIC),
#         (ROCK_MUSIC, ROCK_MUSIC),
#         (COUNTRY_MUSIC, COUNTRY_MUSIC),
#         (DANCE_MUSIC, DANCE_MUSIC),
#         (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
#         (OTHER_MUSIC, OTHER_MUSIC),
#     )
#
#     album_name = models.CharField(
#         max_length=ALBUM_MAX_LEN,
#         unique=True,
#         verbose_name='Album Name',
#     )
#
#     artist = models.CharField(
#         max_length=ALBUM_MAX_LEN,
#     )
#
#     genre = models.CharField(
#         max_length=ALBUM_MAX_LEN,
#         choices=MUSICS,
#     )
#
#     description = models.TextField(
#         null=True,
#         blank=True,
#     )
#
#     image = models.URLField(
#         verbose_name='Image URL',
#     )
#
#     price = models.FloatField(
#         validators=(
#             MinValueValidator(0.0),
#         )
#     )
