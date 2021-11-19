# Create your views here.
from rest_framework import generics
from .serializers import TournamentSerializer
from .serializers import BracketSerializer
from .models import Tournament
from .models import Bracket
import random

from django.http import JsonResponse
import json

class TournamentList(generics.ListCreateAPIView):
    queryset = Tournament.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = TournamentSerializer # tell django what serializer to use

class TournamentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all().order_by('id')
    serializer_class = TournamentSerializer

class BracketList(generics.ListCreateAPIView):
    queryset = Bracket.objects.all().order_by('id')
    serializer_class = BracketSerializer

class BracketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bracket.objects.all().order_by('id')
    serializer_class = BracketSerializer

def join_tourney(request):
    if request.method=='PUT':
        jsonRequest = json.loads(request.body)
        userId = jsonRequest['userId']
        tournamentId = jsonRequest['tournamentId']
        tournament = Tournament.objects.get(id=tournamentId)
        if tournament.limit == tournament.players.all().count():
            return JsonResponse({"added": False})
        else:
            tournament.players.add(userId)
            return JsonResponse({"added": True})

def create_next_round(request):
    if request.method=='PUT':
        jsonRequest = json.loads(request.body)
        userIds = jsonRequest['userIds']
        tournamentId = jsonRequest['tournamentId']
        tournament = Tournament.objects.get(id=tournamentId)
        round = jsonRequest['round']
        list = random.sample(userIds, len(userIds))
        bracket = Bracket(tournament=tournament, round=round)
        bracket.save()
        for id in list:
            bracket.list.add(id)
        return JsonResponse({"id": bracket.id, "tournament": tournamentId, "round": round, "list": list})
