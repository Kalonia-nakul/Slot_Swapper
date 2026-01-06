from rest_framework import serializers
from .models import CustomUser , Slots

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }   

        
class SlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slots
        fields = '__all__'
