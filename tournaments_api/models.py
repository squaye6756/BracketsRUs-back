from django.db import models
import sys
sys.path.append("..")
from user_api.models import User

class Tournament(models.Model):
    name = models.CharField(max_length=32)
    game = models.CharField(max_length=32)
    players = models.ManyToManyField(User, blank=True)
    limit = models.IntegerField()
    complete = models.BooleanField(default=False)
    locked = models.BooleanField(default=False)
    details = models.TextField(blank=True, default='')
    prizes = models.CharField(max_length=100, blank=True, default='None');
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    champion = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='champion')
