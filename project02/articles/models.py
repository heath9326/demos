from django.db import models
from authors.models import Author

class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(blank=False)
    authors = models.ManyToManyField(Author)

    objects = models.Manager()

    def __str__(self):
        return f'Article №{self.id}: "{self.title}"'