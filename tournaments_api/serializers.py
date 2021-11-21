from rest_framework import serializers
from .models import Tournament
from .models import Bracket

class TournamentSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Tournament # tell django which model to use
        fields = ('id', 'name', 'game', 'players', 'limit', 'locked', 'details', 'prizes', 'owner', 'champion') # tell django which fields to include

class BracketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bracket
        fields = ('id', 'tournament', 'round', 'list')
