# Generated by Django 3.2.9 on 2021-11-19 13:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments_api', '0007_auto_20211119_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bracket',
            name='list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
    ]