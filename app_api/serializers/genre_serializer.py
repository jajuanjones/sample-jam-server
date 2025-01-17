from rest_framework import serializers
from app_api.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    """This class will serialize data for genres"""
    class Meta:
        model = Genre
        fields = ('id', 'label')
