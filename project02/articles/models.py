from django.db import models
from authors.models import Author
from accounts.models import CustomUser


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(blank=False)
    authors = models.ManyToManyField(Author)

    objects = models.Manager()

    def __str__(self):
        return f'Article №{self.id}: "{self.title}"'
    
class Comment(models.Model):
    text = models.TextField(max_length=300)
    user = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'Coment №{self.id} by {self.user}'