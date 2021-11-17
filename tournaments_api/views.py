# from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import TournamentSerializer
from .models import Tournament

class TournamentList(generics.ListCreateAPIView):
    queryset = Tournament.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = TournamentSerializer # tell django what serializer to use

class TournamentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all().order_by('id')
    serializer_class = TournamentSerializer
