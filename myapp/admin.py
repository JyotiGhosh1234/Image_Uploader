from django.contrib import admin
from myapp.models import *

# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'date'] 