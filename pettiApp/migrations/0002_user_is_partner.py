# Generated by Django 5.1.1 on 2024-10-08 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pettiApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_partner',
            field=models.BooleanField(default=False),
        ),
    ]