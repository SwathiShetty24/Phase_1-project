from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category,Register,Product,Invoice

admin.site.register(Register)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Invoice)
