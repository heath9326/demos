from django.db import models
from authors.models import Author
from accounts.models import CustomUser

from common.mixins import TimeStampedMixin
from common.models import TimeStampedModel, SlugFieldModel

# Tools
from django.template.defaultfilters import slugify


class Article(TimeStampedModel, SlugFieldModel):
    title = models.CharField(max_length=150)
    text = models.TextField(blank=False)
    authors = models.ManyToManyField(Author, related_name='articles', blank=False)

    objects = models.Manager()

    def __str__(self):
        return f'Article №{self.id}: "{self.title}"'

    def save(self, *args, **kwargs):
        if not self.id:
            #FIXME: ignores russian
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Article, self).save(*args, **kwargs)

    
class Comment(models.Model):
    text = models.TextField(max_length=300)
    user = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'Coment №{self.id} by {self.user}'