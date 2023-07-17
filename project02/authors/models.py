from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # We are using one-to-one connection because one user can be only one author,
    # and author can only be one user
    user = models.OneToOneField(CustomUser, related_name='author', on_delete=models.CASCADE, 
                                null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return f'Author: {self.first_name} {self.last_name}'