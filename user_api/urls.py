from django.urls import path
from . import views

urlpatterns = [
    path('api/users', views.UserList.as_view(), name='user_list'),
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='contact_detail'),
]
