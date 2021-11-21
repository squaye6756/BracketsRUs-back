from django.contrib.postgres.fields import ArrayField
from django.db import models
import sys
sys.path.append("..")
from user_api.models import User

class Tournament(models.Model):
    name = models.CharField(max_length=32)
    game = models.CharField(max_length=32)
    players = models.ManyToManyField(User, blank=True)
    limit = models.IntegerField()
    locked = models.BooleanField(default=False)
    details = models.TextField(blank=True, default='')
    prizes = models.CharField(max_length=100, blank=True, default='None');
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    champion = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='champion')

class Bracket(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    round = models.IntegerField()
    list = ArrayField(models.IntegerField(), blank=True, default=list)
