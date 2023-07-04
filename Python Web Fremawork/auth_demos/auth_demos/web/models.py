from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Article(models.Model):
    created_on = models.DateTimeField()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
    )

    # .......

    user = models.OneToOneField(
        UserModel,
    )
