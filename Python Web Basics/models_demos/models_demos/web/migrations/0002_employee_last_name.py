# Generated by Django 4.2.2 on 2023-06-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
