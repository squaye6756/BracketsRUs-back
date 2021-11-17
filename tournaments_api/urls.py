from django.urls import path
from . import views

urlpatterns = [
    path('api/tournaments', views.TournamentList.as_view(), name='tournaments_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/tournaments/<int:pk>', views.TournamentDetail.as_view(), name='tournaments_detail'), # api/contacts will be routed to the ContactDetail view for handling
]
