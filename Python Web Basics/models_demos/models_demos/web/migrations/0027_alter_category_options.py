# Generated by Django 4.2.2 on 2023-06-15 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_alter_employee_options_department_created_on_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
