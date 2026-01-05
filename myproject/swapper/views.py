from django.shortcuts import render , redirect 
from django.template.loader import render_to_string
import requests
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.http import JsonResponse , HttpResponse

# Create your views here.

@api_view(['GET', 'POST'])  
@permission_classes([AllowAny])
def login(request):
    html = render_to_string('login.html')
    return JsonResponse({'data' : html})


@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated])
def home(request):
    return JsonResponse({"message": "Welcome to the protected home view!"})