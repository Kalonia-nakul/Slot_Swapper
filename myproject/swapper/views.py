from django.shortcuts import render , redirect
import requests 
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
        response = requests.post('http://localhost:8000/api/token/', json={'username': username, 'password': password})
        token = response.json().get('access')
        print("Token:", token)
        return redirect('http://localhost:8000/api/home/?token=' + token)
    return render(request, 'login.html')


@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated])
def home(request):
    return JsonResponse({"message": "Welcome to the protected home view!"})