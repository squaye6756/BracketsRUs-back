# Generated by Django 3.2.9 on 2021-11-18 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
        ('tournaments_api', '0002_auto_20211118_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='players',
            field=models.ManyToManyField(blank=True, to='user_api.User'),
        ),
    ]
