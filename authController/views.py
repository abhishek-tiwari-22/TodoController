from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(["POST"])
def RegisterView(request):
    username=request.data['username']
    password=request.data['password']

    firstname=request.data['FirstName']
    lastname=request.data['LastName']
    email=request.data['Email']
    isactive=request.data['Isactive']
    roles=request.data['Roles']

    user=User(username=username)
    refresh=RefreshToken.for_user(user)
    user.save()

    return Response({'refresh':str(refresh),'access':str(refresh.access_token)})