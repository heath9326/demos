from django.db import models
from authors.models import Author
from accounts.models import CustomUser

from common.mixins import TimeStampedMixin
from common.models import TimeStampedModel, SlugFieldModel

# Tools
from django.template.defaultfilters import slugify
from transliterate import translit

class Article(TimeStampedModel, SlugFieldModel):
    title = models.CharField(max_length=150)
    text = models.TextField(blank=False)
    authors = models.ManyToManyField(Author, related_name='articles')

    objects = models.Manager()

    def __str__(self):
        return f'Article №{self.id}: "{self.title}"'

    def save(self, *args, **kwargs):
        # Set slug only once, to avoid broken links:
        # FIXME: это заплатка:
        if not self.slug or self.slug == 'slug':
            translit_ = translit(self.title, language_code='ru', reversed=True)
            self.slug = slugify(translit_)

        super(Article, self).save(*args, **kwargs)

    
class Comment(models.Model):
    text = models.TextField(max_length=300)
    user = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'Coment №{self.id} by {self.user}'