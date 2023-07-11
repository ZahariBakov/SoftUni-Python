from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size

UserModel = get_user_model()


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='photos',
        validators=(
            validate_file_size,
        )
    )

    description = models.TextField(
        null=True,
        blank=True,
        validators=(
            MinLengthValidator(10),
        )
    )

    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True
    )

    date_of_publication = models.DateField(
        auto_now=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )
