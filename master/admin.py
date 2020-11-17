from django.contrib import admin
from . import models

admin.site.register(models.Comic)
admin.site.register(models.UserComics)

# Register your models here.
