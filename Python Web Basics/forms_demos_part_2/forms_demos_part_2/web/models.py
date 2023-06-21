from django.db import models

from forms_demos_part_2.web.validators import validate_text, ValueInRangeValidator


class Person(models.Model):
    MAX_LEN_NAME = 20

    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )

    profile_image = models.ImageField(
        upload_to='persons',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    MAX_TODO_COUNT_PER_PERSON = 3
    MAX_LEN_TEXT = 25

    text = models.CharField(
        max_length=MAX_LEN_TEXT,
        validators=(
            validate_text,
        ),
    )

    priority = models.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        ),
    )

    is_done = models.BooleanField(
        default=False,
    )

    assignee = models.ForeignKey(
        Person,
        on_delete=models.RESTRICT,
    )
