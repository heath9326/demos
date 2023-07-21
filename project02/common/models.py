from django.db import models
from datetime import datetime


class TimeStampedModel(models.Model):
    ''' Base model for the mixin that creates created_at and 
    updated_at fields '''

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SlugField(models.Model):
    ''' Base model for the mixin that creates a slug field and 
    uses it to overwrite get_absolute_url to use slug '''

    slug = models.SlugField(max_length=50)
    
    def get_absolute_url(self):
        return reverse("article", kwargs=[str(self.slug), str(self.id)])

    class Meta:
        abstract = True