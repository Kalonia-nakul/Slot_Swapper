from rest_framework import serializers
from .models import CustomUser , Slots

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }   

        def create(self, validated_data):
            user = CustomUser(
                username=validated_data['username'],
                email=validated_data['email']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
        
class SlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slots
        fields = '__all__'
