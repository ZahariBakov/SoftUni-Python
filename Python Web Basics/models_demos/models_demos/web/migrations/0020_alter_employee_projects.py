# Generated by Django 4.2.2 on 2023-06-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_project_employee_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(related_name='employees', to='web.project'),
        ),
    ]
