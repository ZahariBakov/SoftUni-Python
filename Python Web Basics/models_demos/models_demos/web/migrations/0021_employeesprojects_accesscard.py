# Generated by Django 4.2.2 on 2023-06-14 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_alter_employee_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeesProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.employee')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.project')),
            ],
        ),
        migrations.CreateModel(
            name='AccessCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.employee')),
            ],
        ),
    ]
