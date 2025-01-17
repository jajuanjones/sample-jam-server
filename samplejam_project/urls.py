"""app_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_api.views import register_user, login_user
from django.conf.urls.static import static
import samplejam_project.settings as settings
from rest_framework.routers import DefaultRouter
from app_api.views import (PostView, GenreView, TagView, 
                           CommentView, CategoryView, ProfileView,
                           UserView, MusicView)

router = DefaultRouter(trailing_slash=False)
router.register(r'posts', PostView, 'post')
router.register(r'genres', GenreView, 'genre')
router.register(r'tags', TagView, 'tag')
router.register(r'comments', CommentView, 'comment')
router.register(r'categories', CategoryView, 'category')
router.register(r'profiles', ProfileView, 'profile')
router.register(r'users', UserView, 'user')
router.register(r'songs', MusicView, 'song')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
