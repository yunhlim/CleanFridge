from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Fridge, User, Ingredient

admin.site.register(User, UserAdmin)
admin.site.register(Ingredient)
admin.site.register(Fridge)
# Register your models here.
