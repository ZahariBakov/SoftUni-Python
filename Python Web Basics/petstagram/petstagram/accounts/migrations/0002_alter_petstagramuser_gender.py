# Generated by Django 4.2.2 on 2023-07-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('do not show', 'DO_NOT_SHOW')], max_length=11),
        ),
    ]
