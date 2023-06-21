from django.contrib import admin

# Register your models here.

from api.models import ToDo

admin.site.register(ToDo)
