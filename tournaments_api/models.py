from django.db import models
import sys
sys.path.append("..")
from user_api.models import User

class Tournament(models.Model):
    name = models.CharField(max_length=32)
    game = models.CharField(max_length=32)
    players = models.ManyToManyField(User)
