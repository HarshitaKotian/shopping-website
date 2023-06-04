from django.contrib import admin

# Register your models here.
from .models import category,Item

admin.site.register(category)
admin.site.register(Item)