from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from apps import users
from apps.users.models import User
from rest_framework import serializers


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.name
        token['id'] = user.id
        return token

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    pass

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'is_active', 'is_staff']
    
    def create(self, validated_data):
        
        user = User.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class DeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'