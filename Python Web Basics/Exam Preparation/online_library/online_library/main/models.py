from django.db import models


class Profile(models.Model):
    MAX_LEN_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        verbose_name='First Name'
    )

    last_name= models.CharField(
        max_length=MAX_LEN_NAME,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name


class Book(models.Model):
    MAX_LEN = 30

    title = models.CharField(
        max_length=MAX_LEN,
    )

    description = models.TextField()

    image = models.URLField()

    type = models.CharField(
        max_length=MAX_LEN,
    )

    def __str__(self):
        return self.title
