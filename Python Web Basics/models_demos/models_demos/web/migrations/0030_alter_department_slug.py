# Generated by Django 4.2.2 on 2023-06-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_fill_slug_for_existing_departments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=models.SlugField(default='none', unique=True),
            preserve_default=False,
        ),
    ]
