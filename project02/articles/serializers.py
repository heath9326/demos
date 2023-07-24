from rest_framework import serializers

from .models import Article, Comment

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

    #TODO: def create, где авторы = список авторов из validated data,  потом for author in authors(Author.)

#FIXME: Doest not regect post form if black=False fields are empty:

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 2