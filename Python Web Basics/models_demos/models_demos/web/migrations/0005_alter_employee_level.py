# Generated by Django 4.2.2 on 2023-06-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_employee_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='level',
            field=models.CharField(max_length=10),
        ),
    ]