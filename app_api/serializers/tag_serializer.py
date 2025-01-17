from rest_framework import serializers
from app_api.models import Tag

class TagSerializer(serializers.ModelSerializer):
    """This class will serialize data for tags"""
    class Meta:
        model = Tag
        fields = ('id', 'label')
