from django.shortcuts import render , redirect
import requests
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from .models import CustomUser
from django.http import JsonResponse , HttpResponse

# Create your views here.

@api_view(['GET', 'POST'])  
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED) 
    return render(request, 'login.html')


@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated])
def home(request):
    return JsonResponse({"message": "Welcome to the protected home view!"})