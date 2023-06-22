# Generated by Django 4.2.2 on 2023-06-22 08:22

import django.core.validators
from django.db import migrations, models
import my_music.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), my_music.web.validators.validate_username]),
        ),
    ]
