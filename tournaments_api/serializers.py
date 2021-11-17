from rest_framework import serializers
from .models import Tournament

class TournamentSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Tournament # tell django which model to use
        fields = ('id', 'name', 'game', 'players') # tell django which fields to include
