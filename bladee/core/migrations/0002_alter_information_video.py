# Generated by Django 4.2 on 2023-05-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='video',
            field=models.FileField(null=True, upload_to='videos'),
        ),
    ]
