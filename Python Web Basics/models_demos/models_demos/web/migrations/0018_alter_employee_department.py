# Generated by Django 4.2.2 on 2023-06-14 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_employee_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.department'),
        ),
    ]