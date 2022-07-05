from rest_framework import serializers
from app_api.models import Music

class MusicSerializer(serializers.ModelSerializer):
    """This class will serialize data for music"""
    class Meta:
        model = Music
        fields = ('id', 'title', 'song', 'genres', 'is_my_song')

class CreateMusicSerializer(serializers.ModelSerializer):
    """This class will serialize data for music"""
    class Meta:
        model = Music
        fields = ['id', 'song', 'title']
