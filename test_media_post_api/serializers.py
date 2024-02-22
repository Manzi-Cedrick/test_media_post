from rest_framework import serializers
from .models import Post, Comment, Drafts, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User,
        fields = ['username','email','password', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)  # Allow the user field to be optional
    class Meta:
        model = Post
        fields = ['title','description','scheduled_datetime','likes','shares','user','draft']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()
    class Meta:
        model = Comment
        fields = ['user','post','comment','created_at','updated_at']
        
class DraftsSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    class Meta:
        model = Drafts
        fields = ['post','created_at','updated_at']