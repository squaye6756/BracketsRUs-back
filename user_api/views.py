# from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

### ALLOWS YOU TO CREATE AND CHECK PASSWORDS
from django.contrib.auth.hashers import make_password, check_password
### ALLOWS YOU TO SEND JSON AS A RESPONSE
from django.http import JsonResponse
### ALLOWS YOU TO TRANSLATE DICTIONARIES INTO JSON DATA
import json

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

### THIS IS THE FUNCTION THAT PERFORMS AUTH
def check_login(request):
        #IF A GET REQUEST IS MADE, RETURN AN EMPTY {}
    if request.method=='GET':
        return JsonResponse({})

        #CHECK IF A PUT REQUEST IS BEING MADE
    if request.method=='PUT':

        jsonRequest = json.loads(request.body) #make the request JSON format
        username = jsonRequest['username'] #get the username from the request
        password = jsonRequest['password'] #get the password from the request
        try:
            if User.objects.get(username=username): #see if username exists in db
                user = User.objects.get(username=username)  #find user object with matching username
                if check_password(password, user.password): #check if passwords match
                    return JsonResponse({'id': user.id, 'username': user.username}) #if passwords match, return a user dict
                else: #passwords don't match
                    return JsonResponse({"error":"Incorrect Password"})
            else: #if username doesn't exist in db, return empty dict
                return JsonResponse({})
        except:
            return JsonResponse({"error":"No Matching Username"})
