# Generated by Django 5.1.3 on 2024-11-26 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom_manager_app', '0003_customuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='division',
        ),
    ]
