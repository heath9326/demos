from rest_framework import serializers

from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        comments = serializers.StringRelatedField(many=True)
        model = Article
        fields = ['title', 'text', 'authors', 'comments']
        depth = 1

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 2