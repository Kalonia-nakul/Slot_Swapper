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
def user_slot_data(request , user):
    if request.method == 'GET' :
        x = CustomUser.objects.get(username=user).id
        print(x)
        slots = Slots.objects.filter(user_id=x)
        print(slots)
        slots_serializer = SlotsSerializer(slots , many = True)
        return Response(slots_serializer.data , status = status.HTTP_200_OK)
    else :
        return Response({"message": "Invalid request method."} , status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def slot_data(request , user):
    if request.method == 'GET' :
        x = CustomUser.objects.get(username=user).id
        slots = Slots.objects.filter().exclude(user_id=x)
        slots_serializer = SlotsSerializer(slots , many = True)
        return Response(slots_serializer.data , status = status.HTTP_200_OK)
    else :
        return Response({"message": "Invalid request method."} , status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_slot(request):
    if request.method == 'POST' :
        data = request.data
        print(data)
        data['user'] = CustomUser.objects.get(username= data['user']).id
        slot_serializer = SlotsSerializer(data = data)
        if slot_serializer.is_valid():
            slot_serializer.save()
            return Response(slot_serializer.data , status = status.HTTP_201_CREATED)
        else :
            return Response(slot_serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    else :
        return Response({"message": "Invalid request method."} , status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST' :
        print(request.data)
        CustomUser.objects.create_user(
            username = request.data['username'],
            email = request.data['email'],
            password = request.data['password']
        )
        return Response({"message": "User registered successfully."} , status = status.HTTP_201_CREATED)    
    else :
        return Response({"message": "Invalid request method."} , status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_slot(request , slot_id):
    if request.method == 'POST' :
        try:
            slot = Slots.objects.get(id=slot_id)
            slot.delete()
            return Response({"message": "Slot deleted successfully."} , status = status.HTTP_200_OK)
        except Slots.DoesNotExist:
            return Response({"message": "Slot not found."} , status = status.HTTP_404_NOT_FOUND)
    else :
        return Response({"message": "Invalid request method."} , status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_swap(request , slot_id):
    if request.method == 'POST' :
        slot_id = request.data.get('slot_id')
        swap_slot_id = request.data.get('swap_slot_id')
        username = request.data.get('username')
         