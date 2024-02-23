from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions
from django.contrib.auth.models import User

class PostList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK )

    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'scheduled_datetime': request.data.get('scheduled_datetime'),
            'likes': request.data.get('likes'),
            'shares': request.data.get('shares'),
            'comments': request.data.get('comments'),
            'draft': request.data.get('draft'),
            'user': request.user.pk
        }
        serializer = PostSerializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
            return Response(post_saved, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    