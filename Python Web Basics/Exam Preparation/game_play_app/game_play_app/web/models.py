from django.core.validators import MinValueValidator
from django.db import models

from game_play_app.web.validators import valid_rating_validator


class Profile(models.Model):
    MAX_LENGTH = 30

    email = models.EmailField()

    age = models.IntegerField(
        validators=(
            MinValueValidator(12),
        ),
    )

    password = models.CharField(
        max_length=MAX_LENGTH,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Game(models.Model):
    TITLE_MAX_LENGTH = 30
    CATEGORY_MAX_LENGTH = 15

    TYPES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other')
    )

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        unique=True,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LENGTH,
        choices=TYPES
    )

    rating = models.FloatField(
        validators=(
            valid_rating_validator,
        ),
    )

    max_level = models.IntegerField(
        MinValueValidator(1),
        blank=True,
        null=True,
    )

    image_url = models.URLField()

    summary = models.TextField(
        blank=True,
        null=True,
    )
