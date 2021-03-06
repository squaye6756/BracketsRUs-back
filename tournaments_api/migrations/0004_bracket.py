# Generated by Django 3.2.9 on 2021-11-18 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
        ('tournaments_api', '0003_alter_tournament_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bracket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField()),
                ('list', models.ManyToManyField(to='user_api.User')),
                ('tournament', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tournaments_api.tournament')),
            ],
        ),
    ]
