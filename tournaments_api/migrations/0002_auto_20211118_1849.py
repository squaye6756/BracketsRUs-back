# Generated by Django 3.2.9 on 2021-11-18 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0001_initial'),
        ('tournaments_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='champion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='champion', to='user_api.user'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournament',
            name='details',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='tournament',
            name='limit',
            field=models.IntegerField(default=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='locked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournament',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='user_api.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='prizes',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
    ]
