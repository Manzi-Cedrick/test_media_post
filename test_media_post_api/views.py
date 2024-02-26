from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment, Drafts
from .serializers import PostSerializer, CommentSerializer, DraftsSerializer
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
    
class PostDetail(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
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
        serializer = PostSerializer(instance=post, data=data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
            return Response(post_saved, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class CommentList(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class CommentDetail(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        post = Post.objects.get(pk)
        
        data = {
            'user': request.user.pk,
            'post': post.pk,
            'comment': request.data.get('comment')
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid(raise_exception = True):
            comment_saved = serializer.save()
            return Response(comment_saved, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        data = {
            'user': request.user.pk,
            'post': request.data.get('post'),
            'comment': request.data.get('comment')
        }
        serializer = CommentSerializer(instance=comment, data=data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()
            return Response(comment_saved, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DraftList(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self):
        drafts = Drafts.objects.all()
        serializer = DraftsSerializer(drafts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DraftDetail(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        drafts = Drafts.objects.get(pk)
        serializer = DraftsSerializer(drafts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        try: 
            post = Post.objects.get(pk)
        except Post.DoesNotExist:
            return Response('Post does not exist', status=status.HTTP_404_NOT_FOUND)
        
        if post.drafts:
            data = {
                'post': post.pk
            }
            serializer = DraftsSerializer(data=data)
            
            if serializer.is_valid(raise_exception=True):
                draft_saved = serializer.save()
                return Response(draft_saved, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response('Post is not a draft', status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        drafts = Drafts.objects.get(pk)
        data = {
            'post': request.data.get('post')
        }
        serializer = DraftsSerializer(instance=drafts, data=data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            draft_saved = serializer.save()
            return Response(draft_saved, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        drafts = Drafts.objects.get(pk)
        drafts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        