# Create your views here.
from rest_framework import generics
from .serializers import TournamentSerializer
from .models import Tournament

from django.http import JsonResponse
import json

class TournamentList(generics.ListCreateAPIView):
    queryset = Tournament.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = TournamentSerializer # tell django what serializer to use

class TournamentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all().order_by('id')
    serializer_class = TournamentSerializer

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
