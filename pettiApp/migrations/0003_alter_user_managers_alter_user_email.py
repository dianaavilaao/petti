# Generated by Django 5.1.1 on 2024-11-05 00:12

import pettiApp.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pettiApp', '0002_user_is_partner'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', pettiApp.managers.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]