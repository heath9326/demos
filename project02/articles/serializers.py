from rest_framework import serializers

from .models import Article, Comment
from authors.models import Author

class CommentSerializeField(serializers.RelatedField):
    """
    A custom field to use in the article serializer.
    """
    def to_representation(self, value):
        return f"Comment '{value.text}' by {value.user.username}"


class ArticleGetSerializer(serializers.ModelSerializer):
    comments = CommentSerializeField(many=True, read_only=True)

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
        instance.title = validated_data["title"]
        instance.text = validated_data["text"]
        author_ids = validated_data["authors"]
        [
            instance.authors.set(author.id)
            for author in author_ids
        ]
        instance.save()
        return instance

    def update(self, instance, validated_data):
        # For simple fields:
        fields = ['title', 'text']
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:
                pass
        
        # For many to many field:
        if "authors" in validated_data:
            author_ids = validated_data.pop("authors")    
            instance.authors.set(author_ids)

        instance.save()
        return instance 
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 2