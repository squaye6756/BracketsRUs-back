# Generated by Django 3.2.9 on 2021-11-19 13:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments_api', '0006_alter_bracket_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bracket',
            name='list',
        ),
        migrations.AddField(
            model_name='bracket',
            name='list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=[], size=None),
        ),
    ]
