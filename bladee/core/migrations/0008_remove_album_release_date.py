# Generated by Django 4.2 on 2023-05-05 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='release_date',
        ),
    ]
