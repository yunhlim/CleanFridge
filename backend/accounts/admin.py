from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Ingredient

admin.site.register(User, UserAdmin)
admin.site.register(Ingredient)

# Register your models here.
