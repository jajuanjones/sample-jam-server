from os import stat
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from app_api.models import Profile, Post
from app_api.serializers import (ProfileSerializer, CreateProfileSerializer,
                                PostSerializer)
from django.core.files.base import ContentFile
import base64
import uuid


# we need to retrieve, list, create, and delete profiles
# we also might need a custom method to add music to a profile
class ProfileView(ViewSet):
    """This view will handle methods for data in profile"""
    def retrieve(self, request, pk):
        """Get a single profile"""
        try:
            profile = Profile.objects.get(pk=pk)
            profile.is_my_profile = request.auth.user == profile.user
            serializer = ProfileSerializer(profile, context={'request': request})
            return Response(serializer.data)
        except Profile.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=False, url_path='my-profile')
    def get_my_profile(self, request):
        user = request.auth.user
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def list(self, request):
        """Get all profiles"""
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={'request': request})
        return Response(serializer.data)
    
    def create(self, request):
        """Create a profile"""
        user = request.auth.user
        tags = request.data['tags']
        serializer = CreateProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(tags=tags, user=user)
        return Response(None, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update a profile"""
        profile = Profile.objects.get(pk=pk)
        # I don't want any data to be required in the response
        # that way if no changes are made to the data it will remain the same
        format, imgstr = request.data["profile_img"].split(';base64,')
        ext = format.split('/')[-1]
        request.data['profile_img'] = ContentFile(base64.b64decode(imgstr), name=f'{request.auth.user.id}-{uuid.uuid4()}.{ext}')
        serializer = CreateProfileSerializer(profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        profile.profile_img = request.data['profile_img']
        profile.save()
        profile.refresh_from_db()
        profile.tags.remove(*profile.tags.all())
        profile.tags.add(*request.data['tags'])
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Delete a profile"""
        profile = Profile.objects.get(pk=pk)
        profile.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['get'], detail=False, url_path="my-posts")
    def get_my_posts(self, request):
        """Get the posts of the user"""
        profile = Profile.objects.get(user=request.auth.user)
        posts = Post.objects.get(profile=profile)
        serializer = PostSerializer(posts)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False, url_path="my-liked-posts")
    def get_my_liked_posts(self, request):
        """Get the posts the user has liked"""
        pass

    @action(methods=['get'], detail=True, url_path="user-posts")
    def get_user_posts(self, request, pk):
        """Get the posts the user has liked"""
        profile = Profile.objects.get(pk=pk)
        posts = Post.objects.get(profile=profile)
        serializer = PostSerializer(posts)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_path="user-liked-posts")
    def get_user_liked_posts(self, request):
        """Get the posts the user has liked"""
        pass
