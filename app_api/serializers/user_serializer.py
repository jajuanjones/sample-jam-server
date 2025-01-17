from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """This class will serialize data for users"""
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')
        
class UpdateUserSerializer(serializers.ModelSerializer):
    """This class will serialize data for updating users"""
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']
