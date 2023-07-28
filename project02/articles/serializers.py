from rest_framework import serializers

from .models import Article, Comment
from authors.models import Author

class ArticleGetSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'text', 'authors', 'comments', 'created_at', 'updated_at', 'slug']
        depth = 1

class ArticleSetSerializer(serializers.ModelSerializer):
    """
    {
        'title': 'title",
        'text': 'text',
        'authors': [
            1, 3, 5, 10
        ]
    }
    """
    class Meta:
        model = Article
        fields = ['title', 'text', 'authors']


    def create(self, validated_data):
        instance = Article.objects.create()
        author_ids = validated_data["authors"]
        instance.title = validated_data["title"]
        instance.text = validated_data["text"]
        [
            instance.authors.add(author.id)
            for author in author_ids
        ]
        instance.save()
        return instance

    #TODO def update:
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 2