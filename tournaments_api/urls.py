from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/tournaments', views.TournamentList.as_view(), name='tournaments_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/brackets', views.BracketList.as_view(), name='brackets_list'),
    path('api/tournaments/<int:pk>', views.TournamentDetail.as_view(), name='tournaments_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('api/brackets/<int:pk>', views.BracketDetail.as_view(), name='brackets_detail'),
    path('api/tournaments/join', csrf_exempt(views.join_tourney), name='join_tournament'),
    path('api/tournaments/next', csrf_exempt(views.create_next_round), name='create_next_round')
]
