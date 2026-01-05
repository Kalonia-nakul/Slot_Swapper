from django.shortcuts import render , redirect 
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from .serializers import CustomUserSerializer , SlotsSerializer
from .models import CustomUser , Slots

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def slot_data(request):
    if request.method == 'GET' :
        slots = Slots.objects.all()
        slots_serializer = SlotsSerializer(slots , many = True)
        return Response(slots_serializer.data , status = status.HTTP_200_OK)

    else :
        return Response({"message": "Invalid request method."} , status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_slot(request):
    if request.method == 'POST' :
        data = request.data.copy()
        data['user'] = CustomUser.objects.get(username=data['user'])
        slot_serializer = SlotsSerializer(data = data)
        if slot_serializer.is_valid():
            slot_serializer.save()
            return Response(slot_serializer.data , status = status.HTTP_201_CREATED)
        else :
            return Response(slot_serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    else :
        return Response({"message": "Invalid request method."} , status = status.HTTP_400_BAD_REQUEST)
    